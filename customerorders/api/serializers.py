from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from customerorders.models import CustomerOrder
from customerprojects.api.serializers import CustomerProjectSerializer

class CustomerOrderSerializer(serializers.ModelSerializer):
    uri       = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomerOrder
        fields=[
            'uri',
            'id',
            'project',
            'order_details',
            'warranty',
            'warranty_type',
            'product_code',
            'serial_no',
            'comments',
            'updated',
            'timestamp',
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-order:detail', kwargs={"id": obj.id}, request=request)