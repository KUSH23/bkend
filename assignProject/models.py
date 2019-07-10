from django.db import models

from accounts.models import User
from customerprojects.models import CustomerProject

class Handle(models.Model): 
    user        = models.CharField(max_length=30)
    project     = models.ForeignKey(CustomerProject, on_delete=models.PROTECT, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.assigned_to)

    class Meta:
        verbose_name = 'Assign project'
        verbose_name_plural = 'Assign projects'


class ChannelPartener(models.Model): 
    channel_partener  = models.CharField(max_length=30)

    def __str__(self):
        return str(self.channel_partener)

    class Meta:
        verbose_name = 'Channel Partener'
        verbose_name_plural = 'Channel Parteners'


class SalesManager(models.Model): 
    sales_manager  = models.CharField(max_length=30)

    def __str__(self):
        return str(self.sales_manager)

    class Meta:
        verbose_name = 'Sales Manager'
        verbose_name_plural = 'Sales Managers'


class Engineer(models.Model): 
    engineer  = models.CharField(max_length=30)

    def __str__(self):
        return str(self.engineer)

    class Meta:
        verbose_name = 'Engineer'
        verbose_name_plural = 'Engineer'