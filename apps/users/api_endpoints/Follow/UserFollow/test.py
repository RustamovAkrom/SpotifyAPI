from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
import faker


fake = faker.Faker()


class UserFollowTest(TestCase):
    def setUp(self):
        # create user
        user = User.objects.create(username="Akromjon")
        user.set_password("2007")
        self.user = user

        # create users
        for _ in range(5):
            User.objects.create(username=fake.name(), email=fake.email())
            user.set_password(fake.password())
            self.user = [].append(user)

        # authentications
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExNzg1NDM1LCJpYXQiOjE3MTExODA2MzUsImp0aSI6Ijc1ZmNjNTAzNDM1OTQxY2FiMzEwM2I3MzE5MmMxMWIyIiwidXNlcl9pZCI6MX0.zIHObqS2Oykeuk4Aw3NaU4l4g7bz1kU7TD0uutNbPQg"
        self.headers = {"Authorization": f"Bearer {self.token}"}
        self.url = reverse("users:follow-user")
        self.data = {"userid": 4}

    def test_follow(self):
        response = self.client.post(self.url, data=self.data, headers=self.headers)
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.json()["detail"], "success")

    def test_are_not_user_follow_user(self):
        data = {"userid": 1}
        response = self.client.post(self.url, data=data, headers=self.headers)
        self.assertEqual(response.json()["detail"], "Akromjon. fail to follow")
