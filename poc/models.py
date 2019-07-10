from django.db import models

from customerprojects.models import CustomerProject

class POC(models.Model): 
    project       = models.ForeignKey(CustomerProject, on_delete=models.CASCADE)
    site_name     = models.CharField(max_length = 30, null=True, blank=True)
    poc_name      = models.CharField(max_length = 30)
    mobile_1      = models.CharField(max_length=10)
    mobile_2      = models.CharField(max_length=10, null=True, blank=True)
    email         = models.EmailField(null=True, blank=True)
    department    = models.CharField(max_length = 30, null=True, blank=True)
    designation   = models.CharField(max_length = 30, null=True, blank=True)

    def __str__(self):
        return str(self.poc_name)

    class Meta:
        verbose_name = 'POC'
        verbose_name_plural = 'POCs'
