from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from customerprojects.models import CustomerProject
from customergroups.api.serializers import CustomerGroupSerializer, SiteSerializer
from place.api.serializers import CountrySerializer, StateSerializer, DistrictSerializer, CitySerializer


class CustomerProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerProject
        fields=[
            'id',
            'group',
            'site_name',
            'sector',
            'country',
            'state',
            'district',
            'city',
            'address',
            'po',
            'po_date',
            'po_type',
            'handled_by',
            'project_id',
            'source',
            'invoice_no',
            'invoice_date',
            'warranty_date',
            'updated',
            'timestamp',
        ]

    # def get_uri(self, obj):
    #     request = self.context.get('request')
    #     return api_reverse('api-project:detail', kwargs={"id": obj.id}, request=request)
        

class CustomerProjectReadSerializer(serializers.ModelSerializer):
    
    group  = CustomerGroupSerializer(read_only=True)
    site_name  = SiteSerializer(read_only=True)
    country  = CountrySerializer(read_only=True)
    state  = StateSerializer(read_only=True)
    district  = DistrictSerializer(read_only=True)
    city  = CitySerializer(read_only=True)
    # total_expense  = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomerProject
        fields=[
            'id',
            'group',
            'site_name',
            'sector',
            'country',
            'state',
            'district',
            'city',
            'address',
            'po',
            'po_date',
            'po_type',
            'handled_by',
            'project_id',
            'source',
            'invoice_no',
            'invoice_date',
            'warranty_date',
            # 'total_expense',
            'updated',
            'timestamp',
        ]
        read_only_fields = ['group', 'country', 'state', 'district', 'site_name', 'city']

    # def get_uri(self, obj):
    #     request = self.context.get('request')
    #     return api_reverse('api-project:detail', kwargs={"id": obj.id}, request=request)
        
    # def get_total_expense(self, obj):
    #     project  = obj.id
    #     total = 0
        
    #     if project is None:
    #         return total
    #     try:    
    #         projects = Ticket.objects.filter(project=project)
    #         print(projects)
    #         for tic in projects:
    #             total += tic.t_expense
    #         formatted_total  = format(total, '.2f') 
    #         return formatted_total
    #     except Exception:
    #         return project
