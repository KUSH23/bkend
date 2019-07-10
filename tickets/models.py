from django.db import models

from customerprojects.models import CustomerProject
from customerorders.models import CustomerOrder
from assignProject.models import SalesManager, Engineer

class Ticket(models.Model): 
    project     = models.ForeignKey(CustomerProject, on_delete=models.CASCADE)
    order       = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, null=True)
    ticket_id   = models.CharField(max_length=30, unique=True)
    request_type= models.CharField(max_length=30, null=True)
    source      = models.CharField(max_length=30)
    sales_manager = models.ForeignKey(SalesManager, on_delete=models.CASCADE, null=True)
    engineer    = models.ForeignKey(Engineer, on_delete=models.CASCADE, null=True)
    comments    = models.TextField(null=True)
    status      = models.CharField(max_length=30, null=True)
    scheduled_date   = models.DateField(null=True)
    start_date   = models.DateField(null=True)
    stop_date    = models.DateField(null=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ticket_id)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'


class Visit(models.Model): 
    ticket      = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comments    = models.TextField()
    expense     = models.DecimalField(default=0.00, max_digits=30, decimal_places=2, null=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.ticket)

    class Meta:
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'
