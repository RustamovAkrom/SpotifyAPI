from rest_framework.serializers import ModelSerializer
from apps.users.models import User


class MiniFollowingsUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class UserFollowingSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "avatar"]
