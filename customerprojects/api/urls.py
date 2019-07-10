from django.conf.urls import url
from django.urls import path

from .views import CustomerProjectAPIView, CustomerProjectAPIDetailView, CustomerProjectCreateAPIView, ProjectAPIDetailView


app_name = "api-project"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('create/', CustomerProjectCreateAPIView.as_view(), name='list-create'),
    url(r'^gr/(?P<group>\d+)/$', ProjectAPIDetailView.as_view(), name='detail'),
    url(r'^(?P<id>\d+)/$', CustomerProjectAPIDetailView.as_view(), name='detail'),
    url('', CustomerProjectAPIView.as_view(), name='list'),
]