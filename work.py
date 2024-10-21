import requests

import os
from django.urls import reverse
from django.core.files import File

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyMTQ4MDI3LCJpYXQiOjE3MTE1NDMyMjcsImp0aSI6IjJiN2NmN2MyNWVlNDQ3NWY5ODU0MTlkYjk4YzIzYzcxIiwidXNlcl9pZCI6MX0.PjscEFhMgnTlssDAVB5i5_aEyThidizP8S5kTePkB3w"


def LoginUser(username: str, password: str):
    url = ""
    user = {"username": username, "password": password}
    response = requests.post(url=url, data=user)

    if response.status_code == 200:
        token = response.json()
        return token["access"]
    else:
        return response.status_code


def main():
    base_url = "http://127.0.0.1:8000"
    # token = LoginUser("Akromjon", "2007")
    # print(token)
    # data = {
    #     "username":"Farux",
    #     "first_name":"Botir",
    #     "last_name":"Abdulayev",
    #     "email":"farux@gmail.com",
    #     "password1":"2007",
    #     "password2":"2007",
    # }
    data = {"username": "Akromjon", "password": "2007"}
    header = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(
        url=base_url + reverse("users:token-obtain-pair"), data=data, headers=header
    )
    print(response.json())
    print(response.status_code)


if __name__ == "__main__":
    import os
    from django.core.asgi import get_asgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    application = get_asgi_application()

    # from rest_framework.authtoken.models import Token
    from apps.users.models import User
    from apps.spotify.models import Artist

    # from rest_framework_simplejwt.tokens import Token

    main()
