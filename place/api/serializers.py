from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from place.models import Country, State, District, City

class CountrySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Country
        fields=[
            'id',
            'country_name',
        ]

class StateSerializer(serializers.ModelSerializer):
    # country  = CountrySerializer(read_only=True)
    class Meta:
        model = State
        fields=[
            'id',
            'country',
            'state_name',
        ]
        # read_only_fields = ['country']

class DistrictSerializer(serializers.ModelSerializer):
    # country  = CountrySerializer(read_only=True)
    # state  = StateSerializer(read_only=True)
    class Meta:
        model = District
        fields=[
            'id',
            'country',
            'state',
            'district_name',
        ]
        # read_only_fields = ['country', 'state']

class CitySerializer(serializers.ModelSerializer):
    # country  = CountrySerializer(read_only=True)
    # state  = StateSerializer(read_only=True)
    # district  = DistrictSerializer(read_only=True)
    class Meta:
        model = City
        fields=[
            'id',
            'country',
            'state',
            'district',
            'city_name',
        ]
        # read_only_fields = ['country', 'state', 'district']