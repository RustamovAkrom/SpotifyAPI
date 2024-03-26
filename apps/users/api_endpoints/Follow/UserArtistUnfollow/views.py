from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .serializers import UserArtistUnfollowSerializer
from apps.spotify.models import Artist
from rest_framework.exceptions import APIException
from django.db import transaction


class UserArtistUnfollowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        user = self.request.user
        serializer = UserArtistUnfollowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        artist_id = serializer.data["artist_id"]
        artist = get_object_or_404(Artist, id=artist_id)
        self.follow_to_artist(user, artist)
        return Response(data={"detail": "success"}, status=status.HTTP_200_OK)

    def follow_to_artist(self, user, artist):
        if artist not in user.artist_followings.all():
            raise APIException("user is not following to artist")
        artist.followers -= 1
        artist.save()
        user.profiles.unfollow_artist(artist)


__all__ = [
    "UserArtistUnfollowAPIView",
]
