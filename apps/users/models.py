from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.shared.models import AbstractBaseModel


class User(AbstractBaseModel, AbstractUser):
    avatar = models.ImageField(
        upload_to="users/avatar/", blank=True, null=True, default="avatar.png"
    )
    token = models.CharField(max_length = 140, unique = True)
    is_active = models.BooleanField(default = False)
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True
    )
    artist_followings = models.ManyToManyField(
        "spotify.Artist", related_name="users", blank=True
    )

    def __str__(self):
        return self.username


class UserProfile(AbstractBaseModel):
    choices_gender = [("female", "Female"), ("male", "Male")]
    user = models.OneToOneField(User, models.CASCADE, related_name="profiles")
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=6, choices=choices_gender, null=True, blank=True
    )
    country = models.CharField(max_length=50, blank=True, null=True)

    def follow(self, user):
        self.user.followings.add(user)

    def unfollow(self, user):
        self.user.followings.remove(user)

    def follow_artist(self, artist):
        self.user.artist_followings.add(artist)

    def unfollow_artist(self, artist):
        self.user.artist_followings.remove(artist)

    def __str__(self):
        return f"{self.user.username} - {self.gender}"


class PlayList(AbstractBaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    title = models.CharField(max_length=120)
    musics = models.ManyToManyField(
        "spotify.Song", related_name="playlists", blank=True
    )

    def __str__(self):
        return self.title
