from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
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
            user = User.objects.create(username=fake.name(), email=fake.email())
            user.set_password(fake.password())
            self.user = [].append(user)

        # authentications
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExNzg1NDM1LCJpYXQiOjE3MTExODA2MzUsImp0aSI6Ijc1ZmNjNTAzNDM1OTQxY2FiMzEwM2I3MzE5MmMxMWIyIiwidXNlcl9pZCI6MX0.zIHObqS2Oykeuk4Aw3NaU4l4g7bz1kU7TD0uutNbPQg"
        self.headers = {"Authorization": f"Bearer {self.token}"}

        # urls
        self.url = reverse("users:followers-user", kwargs={"pk": 1})
        self.url1 = reverse("users:follow-user")

    def test_follow_user(self):

        response = self.client.post(self.url1, data={"userid": 1}, headers=self.headers)
        self.assertEqual(response.status_code, 202)

    def test_followers_list(self):
        response = self.client.get(self.url, headers=self.headers)
        self.assertEqual(type(response.json()), list)
