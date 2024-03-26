from apps.spotify.models import Album
from rest_framework.generics import CreateAPIView
from .serializers import AlbumCreateSerializer


class AlbumCreateAPIView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializer


__all__ = ("AlbumCreateAPIView",)
