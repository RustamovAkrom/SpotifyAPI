from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAuthenticated
from django.urls import path
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="Document Spotify api",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="akromjonrustamov56@gmail.com"),
    ),
    public=True,
    # permission_classes=[IsAuthenticated, ],
    # authentication_classes=[JWTAuthentication, ]
)

# sawgger_urlpatterns = [
#     path('', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
#     path('redoc/', schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc")
# ]

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

drf_swagger_urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
