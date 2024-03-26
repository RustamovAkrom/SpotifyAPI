from rest_framework.generics import RetrieveAPIView
from apps.spotify.models import Artist
from .serializers import ArtistRetriveSerializer


class ArtistRetriveAPIView(RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistRetriveSerializer


__all__ = ("ArtistRetriveAPIView",)
