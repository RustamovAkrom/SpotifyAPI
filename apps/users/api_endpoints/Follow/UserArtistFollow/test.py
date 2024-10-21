from django.test import TestCase
from apps.spotify.models import Artist
from django.urls import reverse
from faker import Faker
from apps.users.tests import AuthenticationTest

fake = Faker()


class UserArtistFollowTest(AuthenticationTest, TestCase):

    def setUp(self):
        for _ in range(5):
            artist = Artist.objects.create(
                first_name=fake.first_name(), last_name=fake.last_name()
            )
            self.artist = artist
        return super().setUp()

    def test_artist_follow(self):
        url = reverse("users:follow-artist")
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {"artist_id": self.artist.id}
        response = self.client.post(url, headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["detail"], "success")
