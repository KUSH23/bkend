from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from .serializers import TicketSerializer, VisitSerializer, TicketReadSerializer
from tickets.models import Ticket, Visit

class TicketAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = TicketSerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ()
    queryset                    = Ticket.objects.all().order_by("-timestamp")
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TicketReadAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = TicketReadSerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ()
    queryset                    = Ticket.objects.all().order_by("-timestamp")
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class TicketAPIDetailView(
    UpdateModelMixin,
    DestroyModelMixin, 
    RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = TicketReadSerializer
    queryset                    = Ticket.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProjectTicketAPIDetailView(TicketReadAPIView):
    serializer_class            = TicketReadSerializer
    def get_queryset(self, *args, **kwargs):
        project = self.kwargs.get("project", None)
        if project is None:
            return Ticket.objects.none()
        return Ticket.objects.filter(project=project).order_by("-timestamp")

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)

class OrderTicketAPIDetailView(TicketReadAPIView):
    serializer_class            = TicketReadSerializer
    def get_queryset(self, *args, **kwargs):
        order = self.kwargs.get("order", None)
        if order is None:
            return Ticket.objects.none()
        return Ticket.objects.filter(order=order).order_by("-timestamp")

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)






class VisitAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = VisitSerializer
    passed_id                   = None
    search_fields               = ('ticket')
    ordering_fields             = ('ticket', 'timestamp')
    queryset                    = Visit.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class VisitAPIDetailView(
    UpdateModelMixin,
    DestroyModelMixin, 
    RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = VisitSerializer
    queryset                    = Visit.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TicketVisitAPIDetailView(VisitAPIView):
    serializer_class            = VisitSerializer
    def get_queryset(self, *args, **kwargs):
        ticket = self.kwargs.get("ticket", None)
        if ticket is None:
            return Visit.objects.none()
        return Visit.objects.filter(ticket=ticket)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)