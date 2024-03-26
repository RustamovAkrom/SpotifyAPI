from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from .serializers import UnfollowSerializer


class UserUnfollowAPIView(APIView):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        user = self.request.user
        data = self.IsData(request)
        serializer = UnfollowSerializer(data)
        user_id = serializer.data["userid"]
        print(user_id)
        following_user = self.get_follow_user(user_id=user_id)
        if self.IsNotOwner(request, following_user):
            self.unfollow_to_user(user, following_user)
            return Response(data={"detail": "you unfollowed"})
        return Response(data={"detail": f"{user}. fail to unfollow"})

    def get_follow_user(self, user_id) -> User:
        user = get_object_or_404(User, id=user_id)
        return user

    def unfollow_to_user(self, user, following_user):
        if following_user.id in [i.id for i in user.followings.all()]:
            user.profiles.unfollow(following_user)
            user.save()
        else:
            raise APIException("You already unfollowing this user")

    def IsNotOwner(self, request, user) -> bool:
        if request.user != user:
            return True
        return False

    def IsData(self, request):
        if not request.data:
            raise APIException({"userid": "this field required"})
        return request.data


__all__ = [
    "UserUnfollowAPIView",
]
