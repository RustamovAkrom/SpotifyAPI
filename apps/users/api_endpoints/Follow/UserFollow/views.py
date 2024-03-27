from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .serializers import FollowSerializer
from apps.users.models import User


class UserFollowAPIView(APIView):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        user = self.request.user
        data = self.IsData(request)
        serializer = FollowSerializer(data)
        user_id = serializer.data["userid"]
        follow_user = self.get_follow_user(user_id)
        if self.IsNotOwner(request, follow_user):
            self.follow_to_user(user, follow_user)
            return Response(data={"detail": "success"}, status=status.HTTP_200_OK)
        return Response(
            data={"detail": f"{user}. fail to follow"}, status=status.HTTP_202_ACCEPTED
        )

    def get_follow_user(self, user_id) -> User:
        user = get_object_or_404(User, id=user_id)
        return user

    def follow_to_user(self, user, following_user):
        if following_user.id in [i.id for i in user.followings.all()]:
            raise APIException("You already follow this user")
        else:
            user.profiles.follow(following_user)
            user.save()

    def IsNotOwner(self, request, user) -> bool:
        if request.user != user:
            return True
        return False

    def IsData(self, request):
        if not request.data:
            raise APIException({"userid": "this fild required"})
        else:
            return request.data


__all__ = [
    "UserFollowAPIView",
]
