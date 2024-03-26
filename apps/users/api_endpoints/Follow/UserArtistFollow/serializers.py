from rest_framework import serializers
from apps.spotify.models import Artist


class UserArtisFollowSerializer(serializers.Serializer):
    artist_id = serializers.CharField(default="")
