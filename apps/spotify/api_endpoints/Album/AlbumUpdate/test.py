
from django.test import TestCase
from apps.spotify.models import Album, Artist
from django.urls import reverse


class AlbumUpdateTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(
            first_name="first_name1", last_name="last_name1"
        )

        self.album = Album.objects.create(title="title1", author=self.artist)

        self.url = reverse("spotify:album-update", kwargs={"pk": self.album.id})

    def test_update(self):
        data = {"title": "new_title1"}
        response = self.client.patch(self.url, data=data, format="json", content_type='application/json')
        self.assertEqual(response.json()['title'], data['title'])
        self.assertEqual(response.status_code, 200)