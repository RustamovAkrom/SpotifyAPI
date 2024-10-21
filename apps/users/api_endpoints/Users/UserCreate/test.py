from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from faker import Faker

from apps.users.models import User

fake = Faker()


class UserCreateTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username="Akromjon",
            email="akromjonrustamov56@gmail.com",
            password="2007",
            is_active=True
        )
        refresh_token = RefreshToken.for_user(self.user)
        self.token = str(refresh_token.access_token)

    def test_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
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
