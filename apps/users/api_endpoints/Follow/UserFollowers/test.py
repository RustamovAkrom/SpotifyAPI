from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
from apps.users.tests import AuthenticationTest
import faker


fake = faker.Faker()


class UserUnfollowTest(AuthenticationTest, TestCase):

    def test_follow_user(self):

        for _ in range(5):
            self.users = User.objects.create(username=fake.user_name())
        self.user = User.objects.create(username="Ahmadjon")
        self.user.profiles.follow(User.objects.last())
        url = reverse("users:followers-user", kwargs={"pk": self.user.id})
        response = self.client.get(url, data={"userid": 1}, headers=self.headers)
        self.assertEqual(response.status_code, 200)
