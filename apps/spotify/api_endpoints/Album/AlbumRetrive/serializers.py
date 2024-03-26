from rest_framework.serializers import ModelSerializer
from apps.spotify.models import Album


class AlbumRetirveSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ("title", "author", "cover")
