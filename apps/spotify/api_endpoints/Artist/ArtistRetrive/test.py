from django.test import TestCase
from django.urls import reverse
from apps.spotify.models import Artist
from faker import Faker

fake = Faker()


class ArtistRetriveTest(TestCase):
    def setUp(self):
        for _ in range(5):
            self.artist = Artist.objects.create(
                first_name=fake.first_name(), last_name=fake.last_name()
            )
        self.url = reverse("spotify:artist-retrive", kwargs={"pk": self.artist.id})

    def test_retrive(self):
        response = self.client.get(self.url)
        self.assertEqual(self.artist.first_name, response.json()["first_name"])
        self.assertEqual(self.artist.last_name, response.json()["last_name"])
        self.assertEqual(response.status_code, 200)
