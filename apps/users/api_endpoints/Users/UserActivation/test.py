from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User
from django.urls import reverse


class UserActivateTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Akrom",
            email="akromjonrustamov56@gmail.com",
            password="password",
            is_active=True,
        )
        refresh_token = RefreshToken.for_user(self.user)
        self.token = str(refresh_token.access_token)

    def test_activation(self):
        activation_user = User.objects.create(
            username="Munisa", email="munisaruziyeva543@gmail.com", password="password"
        )
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        url = reverse("users:user-activation", kwargs={"token": activation_user.token})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["detail"],
            f"{activation_user.username} successfully activated",
        )
