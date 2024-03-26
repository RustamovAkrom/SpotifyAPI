from rest_framework.serializers import ModelSerializer
from apps.spotify.models import Song


class SongRetriveSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ("title", "cover", "file", "genres", "album")
