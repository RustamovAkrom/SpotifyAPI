from django.test import TestCase
from django.urls import reverse
from apps.spotify.models import Song, Genre, Artist, Album
from faker import Faker
import random

fake = Faker()


class TestSongList(TestCase):
    def setUp(self):
        for _ in range(3):
            self.artist = Artist.objects.create(
                first_name=fake.first_name(), last_name=fake.last_name()
            )
            self.album = Album.objects.create(
                title=fake.text(),
                author=random.choice([i for i in Artist.objects.all()]),
            )
            self.genre = Genre.objects.create(name=fake.name())

            data = {
                "title": fake.text(),
                "cover": open("media/artists/avatar/audio_img1.png", "rb"),
                "file": open("D:/musika/Камин EMIN & JONY  TikTok Remix.mp3", "rb"),
                "genres": self.genre.id,
                "album": self.album.id,
            }
            self.client.post(reverse("spotify:song-create"), data=data)
            self.url = reverse("spotify:song-list")

    def test_index(self):
        response = self.client.get(self.url)
        # print(response.json())
        self.assertEqual(response.status_code, 200)
