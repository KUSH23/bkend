from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from poc.models import POC

class POCSerializer(serializers.ModelSerializer):
    uri             = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = POC
        fields=[
            'uri',
            'id',
            'project',
            'site_name',
            'poc_name',
            'mobile_1',
            'mobile_2',
            'email',
            'department',
            'designation',
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-poc:detail', kwargs={"id": obj.id}, request=request)
        
