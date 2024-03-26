from rest_framework.serializers import ModelSerializer

from apps.users.models import User


class MiniFollowersUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class UserFollowersSerializer(ModelSerializer):
    followers = MiniFollowersUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("username", "avatar", "followers")
