import django_filters
from .models import Home

class HomeFilter(django_filters.FilterSet):
    class Meta:
        model = Home
        fields = ['name', 'agent', 'location', 'no_of_rooms', 'area', 'price']
        