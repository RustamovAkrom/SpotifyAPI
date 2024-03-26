from rest_framework.generics import RetrieveAPIView
from apps.spotify.models import Song
from .serializers import SongRetriveSerializer
from django.db import transaction
from rest_framework.response import Response


class SongRetriveAPIView(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongRetriveSerializer

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        song = self.get_object()
        song.listened += 1
        song.save()
        return super().get(request, *args, **kwargs)


__all__ = ("SongRetriveAPIView",)
