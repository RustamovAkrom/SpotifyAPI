from rest_framework.generics import ListAPIView
from apps.spotify.models import Artist
from .serializers import ArtistListSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class ArtistListAPIView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer

    @method_decorator(cache_page(60 * 10))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ("ArtistListAPIView",)
