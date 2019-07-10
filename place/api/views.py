from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import CountrySerializer, StateSerializer, DistrictSerializer, CitySerializer
from place.models import Country, State, District, City

class CountryAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CountrySerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ('timestamp')
    queryset                    = Country.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)





class StateAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = StateSerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ('timestamp')
    queryset                    = State.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StateAPIDetailView(StateAPIView):
    serializer_class            = StateSerializer
    def get_queryset(self, *args, **kwargs):
        country = self.kwargs.get("country", None)
        if country is None:
            return State.objects.none()
        return State.objects.filter(country=country)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)





class DistrictAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = DistrictSerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ('timestamp')
    queryset                    = District.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DistrictAPIDetailView(DistrictAPIView):
    serializer_class            = DistrictSerializer
    def get_queryset(self, *args, **kwargs):
        state = self.kwargs.get("state", None)
        if state is None:
            return District.objects.none()
        return District.objects.filter(state=state)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)






class CityAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CitySerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ('timestamp')
    queryset                    = City.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CityAPIDetailView(CityAPIView):
    serializer_class            = CitySerializer
    def get_queryset(self, *args, **kwargs):
        district = self.kwargs.get("district", None)
        if district is None:
            return City.objects.none()
        return City.objects.filter(district=district)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)