# movies-api/movies/api/urls.py

from django.urls import re_path
from .views import MovieCreateView, MovieDetailView

app_name = 'movies.api'

urlpatterns = [
    re_path(r'^movies/$', MovieCreateView.as_view(), name='movies'),
    re_path(r'^movies/(?P<pk>\d+)/$', MovieDetailView.as_view(), name='detail')
]