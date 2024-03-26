from rest_framework.generics import DestroyAPIView
from apps.spotify.models import Artist
from .serializers import ArtistDestroySerializer


class ArtistDestroyAPIView(DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistDestroySerializer


__all__ = ("ArtistDestroyAPIView",)
