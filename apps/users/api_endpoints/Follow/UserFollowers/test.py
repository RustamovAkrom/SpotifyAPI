from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
import faker

fake = faker.Faker()


class UserUnfollowTest(TestCase):

    def test_follow_user(self):
        url = reverse("users:followers-user")
        response = self.client.post(url, data={"userid": 1}, headers=self.headers)
        self.assertEqual(response.status_code, 202)

#     def test_followers_list(self):
#         response = self.client.get(self.url, headers=self.headers)
#         self.assertEqual(type(response.json()), list)
