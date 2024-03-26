from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.users.models import User
from .serializers import UserListSerializer
from apps.shared.debugger import debugger

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.authentication import TokenAuthentication


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    @method_decorator(cache_page(60 * 10))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @debugger
    def get_queryset(self):
        users = self.queryset.all()
        search = self.request.query_params
        try:
            username = search["username"]
            queryset = users.filter(username__icontains=username)
            return queryset

        except:
            return users


__all__ = [
    "UserListAPIView",
]
