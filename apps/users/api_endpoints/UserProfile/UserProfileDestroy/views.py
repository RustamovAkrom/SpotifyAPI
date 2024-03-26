from rest_framework.generics import DestroyAPIView
from apps.users.models import UserProfile
from .serializers import UserProfileDestroySerializer


class UserProfileDestroyAPIView(DestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDestroySerializer


__all__ = ("UserProfileDestroyAPIView",)
