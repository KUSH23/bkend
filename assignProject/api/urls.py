from django.conf.urls import url
from django.urls import path

from .views import AssignedProjectAPIView, AssignedProjectAPIDetailView, AssignedProjectCreateAPIView, EngineerAPIView, SalesManagerAPIView


app_name = "api-assign"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('create/', AssignedProjectCreateAPIView.as_view(), name='list-create'),
    path('sales_manager/', SalesManagerAPIView.as_view(), name='list-sales_manager'),
    path('engineer/', EngineerAPIView.as_view(), name='list-engineer'),
    url(r'^(?P<id>\d+)/$', AssignedProjectAPIDetailView.as_view(), name='detail'),
    url('', AssignedProjectAPIView.as_view(), name='list'),
]