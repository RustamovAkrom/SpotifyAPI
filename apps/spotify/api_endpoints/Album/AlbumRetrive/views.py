from apps.spotify.models import Album
from rest_framework.generics import RetrieveAPIView
from .serializers import AlbumRetirveSerializer


class AlbumRetriveAPIView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumRetirveSerializer


__all__ = ("AlbumRetriveAPIView",)
