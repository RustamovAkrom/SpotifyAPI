from django.test import TestCase
from apps.users.models import User
from django.urls import reverse
from faker import Faker

fake = Faker()


class UserCreateTest(TestCase):

    def test_create(self):
        url = reverse("users:user-create")
        for _ in range(5):
            password = fake.password()
            data = {
                "username": fake.name(),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "password1": password,
                "password2": password,
            }
            response = self.client.post(url, data=data)
            self.assertEqual(
                response.json()["detail"],
                "Plese activate your profile we have sent an activation link.",
            )
            self.assertEqual(response.status_code, 201)
