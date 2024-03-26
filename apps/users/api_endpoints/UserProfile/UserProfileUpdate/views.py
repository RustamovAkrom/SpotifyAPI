from rest_framework.generics import UpdateAPIView
from apps.users.models import UserProfile
from .serializers import UserProfileUpdateSerializer


class UserProfileUpdateAPIView(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileUpdateSerializer


__all__ = ("UserProfileUpdateAPIView",)
