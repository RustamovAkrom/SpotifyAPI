from rest_framework import serializers


class UserArtistUnfollowSerializer(serializers.Serializer):
    artist_id = serializers.CharField(default="")
