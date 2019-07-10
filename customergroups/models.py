from django.db import models

# Create your models here.

class CustomerGroup(models.Model): 
    group_name   = models.CharField(max_length = 30, unique=True)
    group_prefix = models.CharField(max_length = 30,unique=True)
    # updated     = models.DateTimeField(auto_now=True)
    # timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.group_name)

    class Meta:
        verbose_name = 'Customer Group'
        verbose_name_plural = 'Customer Groups'


class Site(models.Model):
    group = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE)
    site_name   = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.site_name)

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'