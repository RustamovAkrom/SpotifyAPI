from apps.spotify.models import Artist
from rest_framework.serializers import ModelSerializer


class ArtistRetriveSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ("avatar", "first_name", "last_name", "followers")
