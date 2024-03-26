from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
from apps.spotify.models import Artist
import faker


fake = faker.Faker()


class UserUnfollowTest(TestCase):
    def setUp(self):
        # create user
        user = User.objects.create(username="Akromjon")
        user.set_password("2007")
        self.user = user

        # create users
        for _ in range(5):
            artist = Artist.objects.create(
                first_name=fake.first_name(), last_name=fake.last_name()
            )
            self.artist = artist
            self.user.profiles.follow_artist(artist)
            self.user.save()

        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExNzg1NDM1LCJpYXQiOjE3MTExODA2MzUsImp0aSI6Ijc1ZmNjNTAzNDM1OTQxY2FiMzEwM2I3MzE5MmMxMWIyIiwidXNlcl9pZCI6MX0.zIHObqS2Oykeuk4Aw3NaU4l4g7bz1kU7TD0uutNbPQg"
        self.headers = {"Authorization": f"Bearer {self.token}"}
        self.url = reverse("users:unfollow-artist")
        self.url2 = reverse("users:follow-artist")

    def test_unfollow(self):
        data = {"artist_id": self.artist.id}
        response = self.client.post(self.url, data=data, headers=self.headers)
        # print(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["detail"], "success")
