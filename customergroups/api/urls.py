from django.conf.urls import url
from django.urls import path

from .views import CustomerGroupAPIView, CustomerGroupAPIDetailView, SiteAPIDetailView, SiteAPIView


app_name = "api-group"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    url(r'^(?P<id>\d+)/$', CustomerGroupAPIDetailView.as_view(), name='detail'),
    url(r'^sites/(?P<group>\d+)/$', SiteAPIDetailView.as_view(), name='fcity'),
    path('sites/', SiteAPIView.as_view(), name='city-list'),
    path('', CustomerGroupAPIView.as_view(), name='list')
]