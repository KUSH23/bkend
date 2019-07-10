from django.db import models

from customergroups.models import CustomerGroup, Site
from place.models import Country, State, District, City

class CustomerProject(models.Model): 
    group       = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE)
    site_name   = models.ForeignKey(Site, on_delete=models.CASCADE)
    sector      = models.CharField(max_length = 30, null=True, blank=True)
    country     = models.ForeignKey(Country, on_delete=models.CASCADE)
    state       = models.ForeignKey(State, on_delete=models.CASCADE)
    district    = models.ForeignKey(District, on_delete=models.CASCADE)
    city        = models.ForeignKey(City, on_delete=models.CASCADE)
    address     = models.CharField(max_length = 50, null=True, blank=True)
    po          = models.CharField(max_length = 30, null=True, blank=True)
    po_date     = models.DateField(null=True, blank=True)
    po_type     = models.CharField(max_length = 30, null=True, blank=True)
    handled_by  = models.CharField(max_length = 30, null=True, blank=True)
    project_id  = models.CharField(max_length = 30, unique=True, blank=True)
    source      = models.CharField(max_length = 30, null=True, blank=True)
    invoice_no  = models.CharField(max_length = 30, null=True, blank=True)
    invoice_date= models.DateField(null=True, blank=True)
    warranty_date= models.DateField(null=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.project_id)

    class Meta:
        verbose_name = 'Customer Project'
        verbose_name_plural = 'Customer Projects'


