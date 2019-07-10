from django.contrib import admin

from .models import CustomerGroup, Site

admin.site.register(CustomerGroup)
admin.site.register(Site)
