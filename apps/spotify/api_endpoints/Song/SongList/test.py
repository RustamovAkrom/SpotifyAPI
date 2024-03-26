from django.test import TestCase
from django.urls import reverse
from apps.spotify.models import Song, Genre, Artist, Album



class TestSongList(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(
            first_name = "artist_first_name",
            last_name = "artist_last_name"
        )
        self.album = Album.objects.create(
            title = "album1",
            author = 1
        )
        self.genre = Genre.objects.create(name = "genre1")
        self.song = Song.objects.create(
            title = "song1",
            cover = open("media/artists/avatar/audio_img1.png", "rb"),
            file = open("D:/musika/Камин EMIN & JONY  TikTok Remix.mp3", "rb"),
            genres = [self.genre.id],
            album = self.album.id
        )
        self.url = reverse("spotify:song-list")
    def test_index(self):
        response = self.client.get(self.url)
        print(response.json())
        # self.assertEqual(response.status_code, 200)
