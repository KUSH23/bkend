from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import CustomerProjectSerializer, CustomerProjectReadSerializer
from customerprojects.models import CustomerProject

class CustomerProjectCreateAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CustomerProjectSerializer
    passed_id                   = None
    search_fields               = ('group', 'site_name', 'project_id')
    ordering_fields             = ('group', 'timestamp')
    queryset                    = CustomerProject.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CustomerProjectAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CustomerProjectReadSerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ('group_name')
    queryset                    = CustomerProject.objects.all().order_by('group')
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CustomerProjectAPIDetailView(
    UpdateModelMixin,
    DestroyModelMixin, 
    RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CustomerProjectReadSerializer
    queryset                    = CustomerProject.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ProjectAPIDetailView(CustomerProjectAPIView):
    serializer_class            = CustomerProjectReadSerializer
    def get_queryset(self, *args, **kwargs):
        group = self.kwargs.get("group", None)
        if group is None:
            return CustomerProject.objects.none()
        return CustomerProject.objects.filter(group=group)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)