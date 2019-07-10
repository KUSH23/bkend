from django.conf.urls import url
from django.urls import path

from .views import (TicketAPIView, TicketAPIDetailView, ProjectTicketAPIDetailView, TicketReadAPIView,
                    OrderTicketAPIDetailView, VisitAPIView, VisitAPIDetailView, TicketVisitAPIDetailView)


app_name = "api-tickets"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    url(r'^tickets/(?P<id>\d+)/$', TicketAPIDetailView.as_view(), name='detail'),
    url(r'^visits/(?P<id>\d+)/$', VisitAPIDetailView.as_view(), name='vdetail'),
    path('create/', TicketAPIView.as_view(), name='create'),
    path('tickets/', TicketReadAPIView.as_view(), name='list'),
    path('visits/', VisitAPIView.as_view(), name='vlist'),
    url(r'^prtickets/(?P<project>\d+)/$', ProjectTicketAPIDetailView.as_view(), name='p-list'),
    url(r'^odtickets/(?P<order>\d+)/$', OrderTicketAPIDetailView.as_view(), name='o-list'),
    url(r'^ticvisits/(?P<ticket>\d+)/$', TicketVisitAPIDetailView.as_view(), name='t-list'),
]