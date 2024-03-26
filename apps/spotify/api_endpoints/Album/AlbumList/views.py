from apps.spotify.models import Album
from rest_framework.generics import ListAPIView
from .serializers import ALbumListSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class AlbumListAPIView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = ALbumListSerializer

    @method_decorator(cache_page(60 * 10))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ("AlbumListAPIView",)
