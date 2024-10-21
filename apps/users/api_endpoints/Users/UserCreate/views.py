from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserCreateSerializer


class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={
                "detail": "Plese activate your profile we have sent an activation link."
            },
            status=status.HTTP_201_CREATED,
        )


__all__ = ("UserCreateAPIView",)
