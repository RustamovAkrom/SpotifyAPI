from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User
from django.urls import reverse


class UpdatePasswordTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Akromjon", 
            email="akromjonrustamov56@gmail.com",
            password="password",
            is_active=True
        )
        refresh_token = RefreshToken.for_user(self.user)
        self.token = str(refresh_token.access_token)


    def test_update(self):
        url = reverse(
            "users:user-password-update", kwargs={"token": self.user.token}
        )
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        data = {
            "password1": "2007",
            "password2": "2007",
            "email": "akromjonrustamov56@gmail.com",
            "new_password": "0000",
        }
        response = self.client.put(url, data=data)
        
        self.assertEqual(response.status_code, 200)

