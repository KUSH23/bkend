from django.db.models import Sum
import math

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from tickets.models import Ticket, Visit
from customerorders.api.serializers import CustomerOrderSerializer
from customerprojects.api.serializers import CustomerProjectSerializer
from assignProject.api.serializers import SalesManagerSerializer, EngineerSerializer


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields=[
            'id',
            'project',
            'order',
            'ticket_id',
            'request_type',
            'source',
            'sales_manager',
            'engineer',
            'comments',
            'status',
            'scheduled_date',
            'start_date',
            'stop_date',
            'updated',
            'timestamp',
        ]


class TicketReadSerializer(serializers.ModelSerializer):

    project           = CustomerProjectSerializer(read_only=True)
    order             = CustomerOrderSerializer(read_only=True)
    sales_manager     = SalesManagerSerializer(read_only=True)
    engineer          = EngineerSerializer(read_only=True)
    t_expense         = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ticket
        fields=[
            'id',
            'project',
            'order',
            'ticket_id',
            'request_type',
            'source',
            'sales_manager',
            'engineer',
            'comments',
            'status',
            't_expense',
            'scheduled_date',
            'start_date',
            'stop_date',
            'updated',
            'timestamp',
        ]
        read_only_fields = ['project', 'order']

    def get_t_expense(self, obj):
        ticket  = obj.id
        total = 0
        
        if ticket is None:
            return total
        try:    
            visits = Visit.objects.filter(ticket=ticket)
            print(visits)
            for vit in visits:
                total += vit.expense
            formatted_total  = format(total, '.2f') 
            return formatted_total
        except Exception:
            return ticket
       

class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields=[
            'id',
            'ticket',
            'comments',
            'expense',
            'updated',
            'timestamp',
        ]
