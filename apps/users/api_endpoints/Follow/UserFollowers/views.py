from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from .serializers import UserFollowersSerializer

from rest_framework.generics import get_object_or_404


class UserFollowersListAPIView(ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserFollowersSerializer

    def get_queryset(self):
        return get_object_or_404(User, pk=self.kwargs["pk"]).followers.all()


__all__ = [
    "UserFollowersListAPIView",
]
