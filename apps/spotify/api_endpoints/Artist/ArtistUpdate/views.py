from rest_framework.generics import UpdateAPIView
from apps.spotify.models import Artist
from .serializers import ArtistUpdateSerializer


class ArtistUpdateAPIView(UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistUpdateSerializer


__all__ = ("ArtistUpdateAPIView",)
