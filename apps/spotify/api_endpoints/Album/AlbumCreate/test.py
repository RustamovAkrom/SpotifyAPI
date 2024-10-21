from django.test import TestCase
from django.urls import reverse
from apps.spotify.models import Artist


class AlbumCreateTest(TestCase):
    def setUp(self):
        self.url = reverse("spotify:album-create")
        self.artist = Artist.objects.create(
            first_name="first_name1", last_name="last_name1"
        )
        self.data = {"title": "title1", "author": self.artist.id}

    def test_create(self):

        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 201)
