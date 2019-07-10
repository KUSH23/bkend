from django.conf.urls import url
from django.urls import path

from .views import POCAPIView, POCAPIDetailView, ProjectPOCAPIDetailView


app_name = "api-poc"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    url(r'^poc/(?P<id>\d+)/$', POCAPIDetailView.as_view(), name='detail'),
    path('poc/', POCAPIView.as_view(), name='list'),
    url(r'^propoc/(?P<project>\d+)/$', ProjectPOCAPIDetailView.as_view(), name='p-list'),

]