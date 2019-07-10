from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from customergroups.models import CustomerGroup, Site

class CustomerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGroup
        fields=[
            'id',
            'group_name',
            'group_prefix',
        ]


class SiteSerializer(serializers.ModelSerializer):
    # group  = CustomerGroupSerializer(read_only=True)
    class Meta:
        model = Site
        fields=[
            'id',
            'group',
            'site_name',
        ]
        # read_only_fields = ['group']