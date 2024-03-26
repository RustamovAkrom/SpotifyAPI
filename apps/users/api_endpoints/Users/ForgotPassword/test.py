from django.test import TestCase
from apps.users.models import User
from django.urls import reverse


class ForgotPasswordTest(TestCase):
    def setUp(self):
        
        self.user = User.objects.create(
            username = "Akromjon",
            email = "akromjonrustamov56@gmail.com"
        )
        self.user.set_password("2007")
        self.user.save()
        self.url = reverse("users:forgot-password")
    
    def test_forgot(self):

        response = self.client.post(self.url, data={"email":"akromjonrustamov56@gmail.com"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['detail'], f"<{self.user.email}>  we have send an update password link")

    