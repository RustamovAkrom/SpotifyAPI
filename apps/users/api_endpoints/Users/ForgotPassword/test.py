from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User
from django.urls import reverse


class ForgotPasswordTest(APITestCase):
    def setUp(self):

        self.user = User.objects.create(
            username="Akromjon", 
            email="akromjonrustamov56@gmail.com",
            password="password",
            is_active=True
        )

        refres_token = RefreshToken.for_user(self.user)
        self.token = str(refres_token.access_token)

  
    def test_forgot(self):
        url = reverse("users:forgot-password")
        
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

        data={"email": "akromjonrustamov56@gmail.com"}

        response = self.client.post(
            url, data=data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["detail"],
            f"<{self.user.email}>  we have send an update password link",
        )
