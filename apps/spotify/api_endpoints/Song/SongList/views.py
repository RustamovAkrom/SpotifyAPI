from rest_framework.generics import ListAPIView
from apps.spotify.models import Song
from .serializers import SongListSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class SongListAPIView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongListSerializer

    @method_decorator(cache_page(60 * 10))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ("SongListAPIView",)
