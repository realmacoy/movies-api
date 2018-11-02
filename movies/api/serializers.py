# movies-api/movies/api/serializers.py

from rest_framework.serializers import ModelSerializer

from .models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'year_of_release']
        read_only_fields = ['id']
        # extra_kwargs = {
        #     'id': { 'read_only': True}
        # }