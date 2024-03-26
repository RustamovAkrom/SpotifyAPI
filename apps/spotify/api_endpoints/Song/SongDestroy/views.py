from rest_framework.generics import DestroyAPIView
from apps.spotify.models import Song
from .serializers import SongDestroySerializer


class SongDestroyAPIView(DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongDestroySerializer


__all__ = ("SongDestroyAPIView",)
