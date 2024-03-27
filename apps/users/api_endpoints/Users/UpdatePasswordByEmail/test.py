from django.test import TestCase
from apps.users.models import User
from django.urls import reverse


class UpdatePasswordTest(TestCase):
    def setUp(self):
        self.user = User(username="Akromjon", email="akromjonrustamov56@gmail.com")
        self.user.set_password("2007")
        self.user.save()
        self.url = reverse(
            "users:user-password-update", kwargs={"token": self.user.token}
        )

    def test_update(self):
        data = {
            "password1": "2007",
            "password2": "2007",
            "email": "akromjonrustamov56@gmail.com",
            "new_passowrd": "0000",
        }
        response = self.client.options(self.url, data=data)
        self.assertEqual(response.status_code, 200)
