from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
<<<<<<< HEAD
=======
from apps.users.tests import AuthenticationTest
>>>>>>> 8ba28da (update dir in push)
import faker

fake = faker.Faker()


<<<<<<< HEAD
class UserUnfollowTest(TestCase):

    def test_follow_user(self):
        url = reverse("users:followers-user")
        response = self.client.post(url, data={"userid": 1}, headers=self.headers)
        self.assertEqual(response.status_code, 202)


#     def test_followers_list(self):
#         response = self.client.get(self.url, headers=self.headers)
#         self.assertEqual(type(response.json()), list)
=======
class UserUnfollowTest(AuthenticationTest, TestCase):

    def test_follow_user(self):
        for _ in range(5):
            self.users = User.objects.create(username = fake.user_name())
        self.user = User.objects.create(username = "Ahmadjon")
        self.user.profiles.follow(User.objects.last())
        url = reverse("users:followers-user", kwargs={"pk":self.user.id})
        response = self.client.get(url, data={"userid": 1}, headers=self.headers)
        self.assertEqual(response.status_code, 200)
>>>>>>> 8ba28da (update dir in push)
