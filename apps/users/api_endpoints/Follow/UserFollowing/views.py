from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserFollowingSerializer
from apps.users.models import User
from rest_framework.generics import get_object_or_404


class UserFollowingListAPIView(ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserFollowingSerializer

    def get_queryset(self):
        return get_object_or_404(User, pk=self.kwargs["pk"]).followings.all()


__all__ = [
    "UserFollowingListAPIView",
]
