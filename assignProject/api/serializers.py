from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from customerprojects.api.serializers import CustomerProjectReadSerializer
from assignProject.models import Handle, ChannelPartener, SalesManager, Engineer
from accounts.api.serializers import UserPublicSerializer

class AssignedProjectSerializer(serializers.ModelSerializer): 
    user   = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Handle
        fields=[
            'id',
            'user',
            'project',
            'assigned_to',
            'updated',
            'timestamp',
        ]

    def get_user(self, obj):
        request = self.context.get('request')
        user = obj.user
        return user

class AssignedProjectReadSerializer(serializers.ModelSerializer):
    user   = serializers.SerializerMethodField(read_only=True)
    project  = CustomerProjectReadSerializer(read_only=True)
    assigned_to  = UserPublicSerializer(read_only=True)
    
    class Meta:
        model = Handle
        fields=[
            'id',
            'user',
            'project',
            'assigned_to',
            'updated',
            'timestamp',
        ]
        read_only_fields = ['project', 'assigned_to']
        
    def get_user(self, obj):
        request = self.context.get('request')
        user = obj.user
        return user



class SalesManagerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = SalesManager
        fields=[
            'id',
            'sales_manager',
        ]

class EngineerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Engineer
        fields=[
            'id',
            'engineer',
        ]

