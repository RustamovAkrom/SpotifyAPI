from rest_framework.generics import CreateAPIView
from apps.users.models import User
from .serializers import UserCreateSerializer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"detail":"Plese activate your profile we have sent an activation link."})
__all__ = ("UserCreateAPIView",)

