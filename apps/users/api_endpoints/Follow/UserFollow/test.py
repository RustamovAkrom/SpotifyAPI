from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
import faker
from apps.users.tests import AuthenticationTest

fake = faker.Faker()


class UserFollowTest(AuthenticationTest, TestCase):

    def test_follow(self):
        user = User.objects.create(username="Xaker")
        user.set_password("0000")
        user.save()
        data = {"userid": 2}
        url = reverse("users:follow-user")
        response = self.client.post(url, data=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["detail"], "success")
