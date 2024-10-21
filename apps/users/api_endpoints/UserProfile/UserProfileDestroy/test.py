from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User
from django.urls import reverse


class UserProfileDestroyTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            username="Akromjon", 
            password="password", 
            is_active=True
        )

        refresh_token = RefreshToken.for_user(self.user)
        self.token = str(refresh_token.access_token)

    def test_destroy(self):
        url = reverse(
            "users:userprofile-destroy", kwargs={"pk": self.user.profiles.id}
        )
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
