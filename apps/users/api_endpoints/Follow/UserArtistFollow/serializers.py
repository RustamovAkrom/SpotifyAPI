from rest_framework import serializers


class UserArtisFollowSerializer(serializers.Serializer):
    artist_id = serializers.CharField(default="")
