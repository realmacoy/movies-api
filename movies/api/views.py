# movies-api/movies/api/views.py

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Movie
from .serializers import MovieSerializer


class MovieCreateView(ListCreateAPIView):
    lookup_field = 'pk'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
