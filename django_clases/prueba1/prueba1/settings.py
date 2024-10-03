"""


For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------------------------
ENV_SECRET_KEY = os.getenv("SECRET_KEY")

SECRET_KEY = os.getenv("SECRET_KEY")
# -------------------------------------------------------------------------------------

DEBUG = True

# -------------------------------------------------------------------------------------

ALLOWED_HOSTS = []

# -------------------------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Custom apps
    'apps.modulo1',
    'apps.libros'
]
# -------------------------------------------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
# -------------------------------------------------------------------------------------
ROOT_URLCONF = "prueba1.urls"
# -------------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ BASE_DIR / "templates" ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
# -------------------------------------------------------------------------------------
WSGI_APPLICATION = "prueba1.wsgi.application"
# -------------------------------------------------------------------------------------
NAME_DB = os.getenv("NAME_DB")
USER_DB = os.getenv("USER_MYSQL")
PASSWORD_DB =  os.getenv("PASSWORD_MYSQL")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": NAME_DB,
        "USER": USER_DB,
        "PASSWORD": PASSWORD_DB,
        "PORT": '3306'
    }
}
# -------------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# -------------------------------------------------------------------------------------

LANGUAGE_CODE = "es-ar"

TIME_ZONE = "America/Argentina/Buenos_Aires"

USE_I18N = True

USE_TZ = True

# -------------------------------------------------------------------------------------

STATIC_URL = "static/"
STATICFILES_DIRS= BASE_DIR / 'static' ,

MEDIA = "media/"
MEDIA_ROOT = BASE_DIR / 'media',
# -------------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
