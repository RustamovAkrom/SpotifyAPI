from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
from apps.spotify.models import Artist
import faker
from apps.users.tests import AuthenticationTest

fake = faker.Faker()


class UserUnfollowTest(AuthenticationTest, TestCase):
    def test_unfollow(self):
        for _ in range(5):
            user = User.objects.create(username=fake.user_name())
            user.set_password(fake.password())
            user.save()
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {"userid": 2}
        url_unfollow = reverse("users:unfollow-user")
        url_follow = reverse("users:follow-user")
        # follow user
        response1 = self.client.post(url_follow, data=data, headers=headers)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.json()["detail"], "success")
        # unfollow user
        response2 = self.client.post(url_unfollow, data=data, headers=headers)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.json()["detail"], "success")
