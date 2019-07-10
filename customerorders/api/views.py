from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import CustomerOrderSerializer
from customerorders.models import CustomerOrder

class CustomerOrderAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CustomerOrderSerializer
    passed_id                   = None
    search_fields               = ('group_name')
    ordering_fields             = ('group_name', 'timestamp')
    queryset                    = CustomerOrder.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class CustomerOrderAPIDetailView(
    UpdateModelMixin,
    DestroyModelMixin, 
    RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CustomerOrderSerializer
    queryset                    = CustomerOrder.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OrderAPIDetailView(CustomerOrderAPIView):
    serializer_class            = CustomerOrderSerializer
    def get_queryset(self, *args, **kwargs):
        project = self.kwargs.get("project", None)
        if project is None:
            return CustomerOrder.objects.none()
        return CustomerOrder.objects.filter(project=project)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)