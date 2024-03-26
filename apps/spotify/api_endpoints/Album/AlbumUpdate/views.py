from apps.spotify.models import Album
from rest_framework.generics import UpdateAPIView
from .serializers import AlbumUpdateSerializer


class AlbumUpdateAPIView(UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumUpdateSerializer


__all__ = ("AlbumUpdateAPIView",)
