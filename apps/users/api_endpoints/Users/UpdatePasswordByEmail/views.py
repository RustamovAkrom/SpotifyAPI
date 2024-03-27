from rest_framework.views import APIView
from apps.users.models import User
from .serializers import UserPasswordUpdateSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class UserUpdatePasswordAPIView(APIView):
    # queryset = User.objects.all()
    # serializer_class = UserPasswordUpdateSerializer

    def put(self, request, token):
        user = get_object_or_404(User, token=token)
        serializer = UserPasswordUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.data["new_password"]
        user.set_password(new_password)
        user.save()
        return Response(data={"detail": "success"})


__all__ = ("UserUpdatePasswordAPIView",)
