from django.test import TestCase
from apps.users.models import User
from django.urls import reverse
from faker import Faker

fake = Faker()


class UserCreateTest(TestCase):
    def setUp(self):
        self.url = reverse("users:user-create")

    def test_create(self):
        for _ in range(5):
            password = fake.password()
            data = {
                "username": fake.name(),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "password1": password,
                "password2": password,
                "avatar":...
            }
            response = self.client.post(self.url, data=data)
            self.assertEqual(response.status_code, 201)
