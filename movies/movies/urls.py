# movies-api/movies/movies/urls.py

from django.contrib import admin
from django.urls import re_path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    re_path(r'^api/v1/', include(('api.urls', 'movies.api'), namespace='movies-api')),
]
