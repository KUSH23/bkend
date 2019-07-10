from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import POCSerializer
from poc.models import POC  

class POCAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = POCSerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ('timestamp')
    queryset                    = POC.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class POCAPIDetailView(
    UpdateModelMixin,
    DestroyModelMixin, 
    RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = POCSerializer
    queryset                    = POC.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ProjectPOCAPIDetailView(POCAPIView):
    serializer_class            = POCSerializer
    def get_queryset(self, *args, **kwargs):
        project = self.kwargs.get("project", None)
        if project is None:
            return POC.objects.none()
        return POC.objects.filter(project=project)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)