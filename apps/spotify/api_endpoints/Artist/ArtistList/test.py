from django.test import TestCase
from django.urls import reverse
from apps.spotify.models import Artist
from faker import Faker

fake = Faker()


class ArtistListTest(TestCase):
    def setUp(self):
        for _ in range(5):
            self.artist = Artist.objects.create(
                first_name=fake.first_name(), last_name=fake.last_name()
            )
        self.url = reverse("spotify:artist-list")

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.json()), 5)
        self.assertEqual(response.status_code, 200)
