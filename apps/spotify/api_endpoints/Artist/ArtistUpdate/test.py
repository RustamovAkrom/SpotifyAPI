from django.test import TestCase
from django.urls import reverse
from apps.spotify.models import Artist
from faker import Faker


fake = Faker()


class ArtistUpdateTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(
            first_name="first_name1", last_name="last_name1"
        )
        self.url = reverse("spotify:artist-update", kwargs={"pk": self.artist.id})

    def test_update(self):
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
        }
        response = self.client.put(self.url, data=data,format="json", content_type="application/json")
        self.assertEqual(response.json()["first_name"], data['first_name'])
        self.assertEqual(response.json()["last_name"], data['last_name'])
        self.assertEqual(response.status_code, 200)

