import os
import zoneinfo

from pathlib import Path
from django.utils.translation import gettext_lazy as _
from corsheaders.defaults import default_headers

VERSION = "0.0.1"

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")
CORS_ALLOW_HEADERS = (
    *default_headers,
    "Webdeviceuuid",
)
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS", "False").lower() in ("true", "1", "t")
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS").split(" ")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "base.apps.BaseConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

X_FRAME_OPTIONS = "SAMEORIGIN"

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "base/templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "backend.context_processors.global_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"
ASGI_APPLICATION = "backend.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT")
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        }
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ('en-us', _('English')),
    ('it-it', _('Italian')),
)

TIME_ZONES = [(tz, tz) for tz in zoneinfo.available_timezones()]

STATIC_URL = "/static/"
STATIC_ROOT = "/storage/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = "/storage/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": int(os.environ.get("DRF_PAGE_SIZE")),
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
    ),
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle"
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon":"%s/minute" % (os.environ.get("DRF_MAX_REQUESTS_MINUTE")),
        'user':'%s/minute' % (os.environ.get("DRF_MAX_REQUESTS_MINUTE")),
    }
}

DRF_PAGE_SIZE = int(os.environ.get("DRF_PAGE_SIZE"))

DEFAULT_USER_AVATAR_IMAGE_PATH = os.path.join(
    BASE_DIR,
    "internal_media/images/default_user_avatar.jpg"
)

ERROR_CODES = {
    "generic-error": "00001",
    "object-not-found": "00002",
    "forbidden-create": "00003",
    "forbidden-update": "00004",
    "forbidden-list": "00005",
    "forbidden-fetch": "00006",
    "forbidden-delete": "00007",
}