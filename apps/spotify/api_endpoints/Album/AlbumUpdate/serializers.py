from rest_framework.serializers import ModelSerializer
from apps.spotify.models import Album, Artist


class MninAuthorSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ("first_name", "last_name", "avatar")


class AlbumUpdateSerializer(ModelSerializer):
    author = MninAuthorSerializer()

    class Meta:
        model = Album
        fields = ("title", "author", "cover")
