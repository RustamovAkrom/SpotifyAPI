from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.serializers import MyTokenObtainPairSerializer


class MyCustomObtainTokenView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
