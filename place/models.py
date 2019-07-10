from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length = 30, unique=True)

    def __str__(self):
        return str(self.country_name)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name   = models.CharField(max_length = 30, unique=True)

    def __str__(self):
        return str(self.state_name)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'


class District(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state   = models.ForeignKey(State, on_delete=models.CASCADE)
    district_name = models.CharField(max_length = 30, unique=True)

    def __str__(self):
        return str(self.district_name)

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state   = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city_name = models.CharField(max_length = 30, unique=True)

    def __str__(self):
        return str(self.city_name)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'