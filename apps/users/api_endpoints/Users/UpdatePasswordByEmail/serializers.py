from rest_framework.serializers import Serializer, ModelSerializer
from apps.users.models import User
from rest_framework import fields
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404


class UserPasswordUpdateSerializer(ModelSerializer):
    password1 = fields.CharField(max_length=120)
    password2 = fields.CharField(max_length=120)
    email = fields.EmailField()
    new_password = fields.CharField(max_length=120)

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise ValidationError("password1 and password2 is not match")
        return attrs

    def validate_email(self, value):
        if value not in [i.email for i in User.objects.all()]:
            raise ValidationError("Is not valid your email")
        return value

    class Meta:
        model = User
        fields = ("password1", "password2", "email", "new_password")
