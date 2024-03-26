from django.test import TestCase
from apps.spotify.models import Genre, Album, Artist
import json
from django.core.files import File

url = "http://127.0.0.1:8000/api/v1/spotify/song-create/"


class TestSongCreate(TestCase):
    def setUp(self):
        artist = Artist.objects.create(first_name="first_name1", last_name="last_name1")
        self.artist = artist

        genre = Genre.objects.create(name="Pop")
        self.genre = genre

        album = Album.objects.create(title="album1", author=self.artist)
        self.album = album

    def test_create_song(self):
        data = {
            "title": "title1",
            "cover": open("media/artists/avatar/audio_img1.png", "rb"),
            "file": open("D:/musika/Камин EMIN & JONY  TikTok Remix.mp3", "rb"),
            "genres": self.genre.id,
            "album": self.album.id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
