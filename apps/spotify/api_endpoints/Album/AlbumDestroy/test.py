from django.test import TestCase
from django.urls import reverse
from apps.spotify.models import Album, Artist


class AlbumDestroyTest(TestCase):
    def setUp(self):
        artist = Artist.objects.create(first_name="first_name1", last_name="last_name1")
        self.artist = artist
        album = Album.objects.create(title="title1", author=self.artist)
        self.album = album

        self.url = reverse("spotify:album-destroy", kwargs={"pk": self.album.id})

    def test_destroy(self):
        response = self.client.delete(self.url, data={"detail": self.album.id})
        self.assertEqual(response.status_code, 204)
