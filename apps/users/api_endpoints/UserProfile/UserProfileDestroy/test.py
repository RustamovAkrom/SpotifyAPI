from django.test import TestCase
from apps.users.models import UserProfile, User
from django.urls import reverse


class UserProfileDestroyTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = "Akromjon"
        )
        self.user.set_password("2007")

        self.url = reverse("users:userprofile-destroy", kwargs={"pk":self.user.profiles.id})

    def test_destroy(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)