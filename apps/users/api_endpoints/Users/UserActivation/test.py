from django.test import TestCase
from apps.users.models import User
from django.urls import reverse


class UserActivateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Munisa", email="akromjonrustamov56@gmail.com"
        )
        self.user.set_password("0000")
        self.user.save()

        self.url = reverse("users:user-activation", kwargs={"token": self.user.token})

    def test_activation(self):
        data = {}
        response = self.client.get(self.url, data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["detail"], f"{self.user.username} successfully activated"
        )
