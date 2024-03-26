from apps.spotify.models import Album
from rest_framework.generics import DestroyAPIView
from .serializers import AlbumDestroySerializer


class AlbumDestroyAPIView(DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDestroySerializer


__all__ = ("AlbumDestroyAPIView",)
