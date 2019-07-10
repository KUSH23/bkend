from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import CustomerGroupSerializer, SiteSerializer
from customergroups.models import CustomerGroup, Site

class CustomerGroupAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CustomerGroupSerializer
    passed_id                   = None
    search_fields               = ('group_name')
    ordering_fields             = ('group_name', 'timestamp')
    queryset                    = CustomerGroup.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class CustomerGroupAPIDetailView(
    UpdateModelMixin,
    DestroyModelMixin, 
    RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CustomerGroupSerializer
    queryset                    = CustomerGroup.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SiteAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = SiteSerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ('timestamp')
    queryset                    = Site.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SiteAPIDetailView(SiteAPIView):
    serializer_class            = SiteSerializer
    def get_queryset(self, *args, **kwargs):
        group = self.kwargs.get("group", None)
        if group is None:
            return Site.objects.none()
        return Site.objects.filter(group=group)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)