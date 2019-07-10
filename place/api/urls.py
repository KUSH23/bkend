from django.conf.urls import url
from django.urls import path

from .views import CountryAPIView, StateAPIDetailView, StateAPIView, DistrictAPIView, DistrictAPIDetailView, CityAPIView, CityAPIDetailView

app_name = "api-place"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('countries/', CountryAPIView.as_view(), name='countries'),
    path('states/', StateAPIView.as_view(), name='state-list'),
    url(r'^states/(?P<country>\d+)/$', StateAPIDetailView.as_view(), name='fstates'),
    path('districts/', DistrictAPIView.as_view(), name='district-list'),
    url(r'^districts/(?P<state>\d+)/$', DistrictAPIDetailView.as_view(), name='fdistrict'),
    path('cities/', CityAPIView.as_view(), name='city-list'),
    url(r'^cities/(?P<district>\d+)/$', CityAPIDetailView.as_view(), name='fcity'),
    
]