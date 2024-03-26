from django.test import TestCase
from apps.spotify.models import Artist
from django.urls import reverse
from faker import Faker

fake = Faker()


class ArtistCreateTest(TestCase):
    def setUp(self):
        self.url = reverse("spotify:artist-create")

    def test_create(self):
        for _ in range(5):
            data = {"first_name": fake.first_name(), "last_name": fake.last_name()}
            response = self.client.post(self.url, data=data)
            self.assertEqual(response.status_code, 201)
