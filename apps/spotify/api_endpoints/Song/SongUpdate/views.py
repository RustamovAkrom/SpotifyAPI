from rest_framework.generics import UpdateAPIView
from apps.spotify.models import Song
from .serializers import SongUpdateSerializer


class SongUpdateAPIView(UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongUpdateSerializer


__all__ = ("SongUpdateAPIView",)
