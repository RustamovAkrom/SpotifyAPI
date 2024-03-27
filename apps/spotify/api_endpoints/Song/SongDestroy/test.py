from django.test import TestCase
from apps.spotify.models import Album, Genre, Artist, Song
from rest_framework.test import APITestCase
from django.urls import reverse


class TestSongDestroy(TestCase):

    def setUp(self):

        self.artist = Artist.objects.create(
            first_name="first_name1", last_name="last_name1"
        )
        self.genre = Genre.objects.create(name="Pop")
        self.album = Album.objects.create(title="album12", author=self.artist)

        data = {
            "title": "title1",
            "cover": open("media/artists/avatar/audio_img1.png", "rb"),
            "file": open("D:/musika/Камин EMIN & JONY  TikTok Remix.mp3", "rb"),
            "genres": self.genre.id,
            "album": self.album.id,
        }
        self.client.post(reverse("spotify:song-create"), data=data)
        self.song = Song.objects.get(title="title1")

        self.url = reverse("spotify:song-destroy", kwargs={"pk": self.song.id})

    def test_delete_song(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
