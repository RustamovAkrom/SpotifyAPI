from rest_framework.serializers import ModelSerializer
from apps.users.models import User
from rest_framework import fields
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(ModelSerializer):
    username = fields.CharField(max_length=120)
    first_name = fields.CharField(max_length=120)
    last_name = fields.CharField(max_length=120)
    email = fields.EmailField()
    password1 = fields.CharField(max_length=120)
    password2 = fields.CharField(max_length=120)
    avatar = fields.ImageField(default="avatar.jpeg")

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise ValidationError("password1 and password2 must match")
        return attrs

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("Username already taken")
        return value
    
    def validate_email(self, value):
        if value in [i.email for i in User.objects.all()]:
            raise ValidationError("your email already exist")
        return value
    
    def create(self, validated_data):
        username = validated_data.get("username")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        password = validated_data.get("password1")
        email = validated_data.get("email")
        avatar = validated_data.get("avatar")

        user = User.objects.create(
            username=username,
            first_name=first_name,
            
            last_name=last_name,
            avatar=avatar,
            email=email,
        )
        user.set_password(password)
        user.save()
        return validated_data

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "avatar",
        )
