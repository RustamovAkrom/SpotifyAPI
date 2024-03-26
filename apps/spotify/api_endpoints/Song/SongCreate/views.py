from rest_framework.generics import CreateAPIView
from apps.spotify.models import Song
from .serializers import SongCreateSerializer


class SongCreateAPIView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongCreateSerializer


__all__ = ("SongCreateAPIView",)
