DJANGO_DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
PROJECT_APPS = [
    "apps.shared.apps.SharedConfig",
    "apps.spotify.apps.SpotifyConfig",
    "apps.users.apps.UsersConfig",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "django_celery_beat",
    "django_celery_results",
]
