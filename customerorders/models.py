from django.db import models

from customerprojects.models import CustomerProject

class CustomerOrder(models.Model): 
    project       = models.ForeignKey(CustomerProject, on_delete=models.CASCADE)
    order_details = models.CharField(max_length = 30, null=True, blank=True)
    warranty      = models.DateField(null=True, blank=True)
    warranty_type = models.CharField(max_length = 30, null=True, blank=True)
    product_code  = models.CharField(max_length = 30, null=True, blank=True)
    serial_no     = models.CharField(max_length = 30, null=True, blank=True)
    comments      = models.TextField(null=True, blank=True)
    updated       = models.DateTimeField(auto_now=True)
    timestamp     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_code)

    class Meta:
        verbose_name = 'CustomerOrder'
        verbose_name_plural = 'CustomerOrders'
