from django.test import TestCase
from apps.spotify.models import Album, Artist
from django.urls import reverse
from faker import Faker


fake = Faker()


class AlbumListTest(TestCase):
    def setUp(self):
        for _ in range(5):
            artist = Artist.objects.create(
                first_name=fake.first_name(), last_name=fake.last_name()
            )
            self.artist = artist
            Album.objects.create(title=fake.name(), author=self.artist)
            self.albums = Album.objects.all()

        self.url = reverse("spotify:album-list")

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_data(self):
        response = self.client.get(self.url)
        data = len(response.json())
        self.assertEqual(data, 5)
