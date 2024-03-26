from typing import Iterable
import uuid
from django.db import models

from apps.shared.models import AbstractBaseModel


class Genre(AbstractBaseModel):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name


class Artist(AbstractBaseModel):
    id = models.UUIDField(primary_key=True)
    avatar = models.ImageField(
        upload_to="artists/avatar/", blank=True, null=True, default="avatar.jpeg"
    )
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=130)
    followers = models.IntegerField(default=0)

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: str | None = None,
        update_fields: Iterable[str] | None = None,
    ):
        if not self.id:
            self.id = uuid.uuid4()
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Album(AbstractBaseModel):
    title = models.CharField(max_length=120)
    author = models.ForeignKey("spotify.Artist", models.CASCADE)
    cover = models.ImageField(
        upload_to="albums/cover/", blank=True, null=True, default="album.png"
    )

    def __str__(self):
        return self.title


class Song(AbstractBaseModel):
    title = models.CharField(max_length=120)
    cover = models.ImageField(upload_to="songs/cover/")
    file = models.FileField(upload_to="songs/file/")
    genres = models.ManyToManyField("spotify.Genre")
    album = models.ForeignKey("spotify.Album", models.DO_NOTHING, "songs")
    listened = models.IntegerField(default=0)

    def __str__(self):
        return self.title
