import os

# CACHES = {
#     "default": "django_redis.cache.RedisCache",
#     "LOCATION": os.getenv("REDIS_CACHE_URL"),
#     "OPTIONS": {"CLIENTS_CLASS": "django_redis.client.DefaultClient"},
#     "KEY_PREFIX": "core"
# }

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",
    }
}

CACHE_MIDDLEWARE_SECONDS = str(os.getenv("CACHE_TIMOUT"))

CELERY_BROKER_URL = str(os.getenv("CELERY_BROKER", "REDIS://redis:6379/0"))
CELERY_RESULT_BACKEND = str(os.getenv("RABBITMQ_RESULT_BACKEND"))
