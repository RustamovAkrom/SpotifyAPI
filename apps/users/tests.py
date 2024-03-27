from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
from apps.spotify.models import Album, Artist, Genre, Song
from faker import Faker
import random

fake = Faker()


# Create your tests here.
class AuthenticationTest(TestCase):
    def setUp(self):
        self.user = User(username="Botirjon", is_active=True)
        self.user.set_password("2007")
        self.user.save()

        self.url = reverse("users:token-obtain-pair")
        data = {"username": self.user.username, "password": "2007"}
        response = self.client.post(
            self.url, data=data, format="json", content_type="application/json"
        )
        self.token = response.json()["access"]
        self.headers = {"Authorization": f"Bearer {self.token}"}
