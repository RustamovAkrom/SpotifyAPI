from rest_framework.generics import CreateAPIView
from apps.spotify.models import Artist
from .serializers import ArtistCreateSerializer


class ArtistCreateAPIView(CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistCreateSerializer


__all__ = ("ArtistCreateAPIView",)
