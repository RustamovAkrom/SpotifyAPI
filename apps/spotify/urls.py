from django.urls import path

from .api_endpoints.Song import (
    SongDestroyAPIView,
    SongCreateAPIView,
    SongListAPIView,
    SongRetriveAPIView,
    SongUpdateAPIView,
)
from .api_endpoints.Album import (
    AlbumDestroyAPIView,
    AlbumCreateAPIView,
    AlbumListAPIView,
    AlbumRetriveAPIView,
    AlbumUpdateAPIView,
)
from .api_endpoints.Artist import (
    ArtistCreateAPIView,
    ArtistDestroyAPIView,
    ArtistListAPIView,
    ArtistRetriveAPIView,
    ArtistUpdateAPIView,
)

app_name = "spotify"

urlpatterns = [
    path("song-destroy/<pk>", SongDestroyAPIView.as_view(), name="song-destroy"),
    path("song-create/", SongCreateAPIView.as_view(), name="song-create"),
    path("song-list/", SongListAPIView.as_view(), name="song-list"),
    path("song-retrive/<pk>", SongRetriveAPIView.as_view(), name="song-retrive"),
    path("song-update/<pk>", SongUpdateAPIView.as_view(), name="song-update"),
    path("album-destroy/<pk>", AlbumDestroyAPIView.as_view(), name="album-destroy"),
    path("album-create/", AlbumCreateAPIView.as_view(), name="album-create"),
    path("album-list/", AlbumListAPIView.as_view(), name="album-list"),
    path("album-retrive/<pk>", AlbumRetriveAPIView.as_view(), name="album-retrive"),
    path("album-update/<pk>", AlbumUpdateAPIView.as_view(), name="album-update"),  #
    path("artist-destroy/<pk>", ArtistDestroyAPIView.as_view(), name="artist-destroy"),
    path("artist-create/", ArtistCreateAPIView.as_view(), name="artist-create"),
    path("artist-list/", ArtistListAPIView.as_view(), name="artist-list"),
    path("artist-retrive/<pk>", ArtistRetriveAPIView.as_view(), name="artist-retrive"),
    path("artist-update/<pk>", ArtistUpdateAPIView.as_view(), name="artist-update"),
]
