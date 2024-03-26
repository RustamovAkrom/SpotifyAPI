from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from apps.users.models import User


class UserActivationAPIView(APIView):
    def get(self, request, token):
        user = get_object_or_404(User, token = token)
        user.is_active = True
        user.save()
        return Response(data={"detail": f"{user.username} successfully activated"})
    
__all__ = ("UserActivationAPIView", )