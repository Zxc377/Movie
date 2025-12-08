from .models import Movie
from django_filters import FilterSet


class MovieFilter(FilterSet):

    class Meta:
        model = Movie
        fields = {
            'country':['exact'],
            'year':['gte','lte'],
            'genre':['exact'],
            'director':['exact'],
            'actor':['exact'],



        }