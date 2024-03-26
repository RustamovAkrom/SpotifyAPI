from rest_framework.serializers import ModelSerializer
from apps.users.models import UserProfile


class UserProfileDestroySerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("user", "email", "birthday", "gender", "country")
