from apps.spotify.models import Artist
from rest_framework.serializers import ModelSerializer


class ArtistDestroySerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ("avatar", "frist_name", "last_name", "followers")
