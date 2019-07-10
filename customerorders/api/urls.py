from django.conf.urls import url
from django.urls import path

from .views import CustomerOrderAPIView, CustomerOrderAPIDetailView, OrderAPIDetailView


app_name = "api-order"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    url(r'^orders/(?P<id>\d+)/$', CustomerOrderAPIDetailView.as_view(), name='detail'),
    path('orders/', CustomerOrderAPIView.as_view(), name='list'),
    url(r'^prorder/(?P<project>\d+)/$', OrderAPIDetailView.as_view(), name='p-list'),
]