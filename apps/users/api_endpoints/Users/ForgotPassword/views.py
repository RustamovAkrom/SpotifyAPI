import os

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from apps.users.models import User

from dotenv import load_dotenv

load_dotenv()


class ForgotPasswordAPIView(APIView):

    @method_decorator(cache_page(60 * 10))
    def post(self, request):
        email = request.data["email"]
        user = get_object_or_404(User, email=email)
        email_host_user = os.getenv("EMAIL_HOST_USER")

        send_mail(
            subject="Update password link",
            message=f"password update link -> http://localhost:8000/api/v1/users/user-password-update/{user.token}",
            from_email=email_host_user,
            recipient_list=[user.email],
        )

        return Response(
            data={"detail": f"<{user.email}>  we have send an update password link"}
        )


__all__ = ("ForgotPasswordAPIView",)
