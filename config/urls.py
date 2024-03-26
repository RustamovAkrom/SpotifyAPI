from django.contrib import admin
from django.conf.urls.static import static
from config import settings
from django.urls import path, include
from .swagger import drf_swagger_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("apps.users.urls")),
    path("api/v1/spotify/", include("apps.spotify.urls")),
]

urlpatterns += drf_swagger_urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
