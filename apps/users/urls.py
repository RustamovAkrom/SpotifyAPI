from django.urls import path
from .api_endpoints.Follow import *
from .api_endpoints.Users import *
from .api_endpoints.UserProfile import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import MyCustomObtainTokenView

app_name = "users"
urlpatterns = [
    path("token/", MyCustomObtainTokenView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    # follow
    path("follow-user/", UserFollowAPIView.as_view(), name="follow-user"),
    path("unfollow-user/", UserUnfollowAPIView.as_view(), name="unfollow-user"),
    path("follow-artist/", UserArtistFollowAPIView.as_view(), name="follow-artist"),
    path(
        "unfollow-artist/", UserArtistUnfollowAPIView.as_view(), name="unfollow-artist"
    ),
    path(
        "followers-user/<pk>", UserFollowersListAPIView.as_view(), name="followers-user"
    ),
    path(
        "followings-user/<pk>",
        UserFollowingListAPIView.as_view(),
        name="followings-user",
    ),
    # users
    path(
        "user-forgot-password/", ForgotPasswordAPIView.as_view(), name="forgot-password"
    ),
    path(
        "user-password-update/<str:token>",
        UserUpdatePasswordAPIView.as_view(),
        name="user-password-update",
    ),
    path(
        "user-activation/<str:token>",
        UserActivationAPIView.as_view(),
        name="user-activation",
    ),
    path("user-list/", UserListAPIView.as_view(), name="user-list"),
    path("user-create/", UserCreateAPIView.as_view(), name="user-create"),
    # userprofiles
    path(
        "userprofile-destroy/<pk>",
        UserProfileDestroyAPIView.as_view(),
        name="userprofile-destroy",
    ),
    path(
        "userprofile-update/<pk>",
        UserProfileUpdateAPIView.as_view(),
        name="userprofile-update",
    ),
]
