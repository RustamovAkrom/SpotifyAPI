from django.test import TestCase
from apps.spotify.models import Album, Artist
from django.urls import reverse
from faker import Faker
import random

fake = Faker()


class AlbumRetriveTest(TestCase):
    def setUp(self):
        for _ in range(5):
            self.artist = Artist.objects.create(
                first_name=fake.first_name(), last_name=fake.last_name()
            )
        for _ in range(5):
            self.album = Album.objects.create(
                title=fake.text(), author=random.choice(Artist.objects.all())
            )
        self.url = reverse("spotify:album-retrive", kwargs={"pk": 1})

    def test_retrive(self):
        response = self.client.get(self.url)
        self.assertEqual(
            response.headers["Allow"].split(", "), ["GET", "HEAD", "OPTIONS"]
        )
        self.assertEqual(response.status_code, 200)
