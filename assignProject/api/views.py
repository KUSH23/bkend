from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import AssignedProjectSerializer, AssignedProjectReadSerializer, SalesManagerSerializer, EngineerSerializer
from assignProject.models import Handle, ChannelPartener, SalesManager, Engineer

class AssignedProjectCreateAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = AssignedProjectSerializer
    passed_id                   = None
    search_fields               = ('group', 'site_name', 'project_id')
    ordering_fields             = ('group', 'timestamp')
    queryset                    = Handle.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AssignedProjectAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = AssignedProjectReadSerializer
    passed_id                   = None
    search_fields               = ('group', 'site_name', 'project_id')
    ordering_fields             = ('group', 'timestamp')
    queryset                    = Handle.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AssignedProjectAPIDetailView(
    UpdateModelMixin,
    DestroyModelMixin, 
    RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = AssignedProjectReadSerializer
    queryset                    = Handle.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SalesManagerAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = SalesManagerSerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ('timestamp')
    queryset                    = SalesManager.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EngineerAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = EngineerSerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ('timestamp')
    queryset                    = Engineer.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
