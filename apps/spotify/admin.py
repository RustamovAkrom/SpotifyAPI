from django.contrib import admin
from .models import Album, Genre, Song, Artist

admin.site.register([Album, Genre, Song])


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    fields = ["avatar", "first_name", "last_name", "followers"]
    list_display = ["first_name", "last_name", "avatar", "followers", "id"]
