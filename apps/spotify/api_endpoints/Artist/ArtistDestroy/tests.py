from django.test import TestCase
from django.urls import reverse
from apps.spotify.models import Artist


class ArtistDestroyTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(
            first_name="first_name1", last_name="last_name1"
        )

        self.url = reverse("spotify:artist-destroy", kwargs={"pk": self.artist.id})

    def test_destroy(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
