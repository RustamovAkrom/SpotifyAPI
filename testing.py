import requests

import os
from django.urls import reverse
from django.core.files import File

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExNzg1NDM1LCJpYXQiOjE3MTExODA2MzUsImp0aSI6Ijc1ZmNjNTAzNDM1OTQxY2FiMzEwM2I3MzE5MmMxMWIyIiwidXNlcl9pZCI6MX0.zIHObqS2Oykeuk4Aw3NaU4l4g7bz1kU7TD0uutNbPQg"


def LoginUser(username: str, password: str):
    url = ''
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
    #     "username":"Begzod",
    #     "first_name":"Botir",
    #     "last_name":"Abdulayev",
    #     "email":"diril87023@shaflyn.com",
    #     "password1":"2007",
    #     "password2":"2007",
    #     # "avatar": open("media/avatar.png", "rb")
    # }
    data = {
        "email":"akromjonrustamov56@gmail.com"
    }
    header = {'content-type': 'application/json'}
    response = requests.post(url = base_url + reverse("users:forgot-password"), data=data)#{"email":"akromjonrustamov56@gmail.com"})
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
