

import os
from pathlib import Path
from django.contrib.messages import constants as messages
from dotenv import load_dotenv, find_dotenv
# import dj_database_url


load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q0nj!x(fgrj37c$_f!9d_sn-dbg)r!aw!+6lu0$lm$b@u_v#bv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "certificates_database",
    "members",
    "accounts",
    "dashboard",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "certify.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "certify.wsgi.application"




# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600),
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"), "./static/",
]

STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR/ 'media'
MEDIA_URL = '/media/'
#STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://:p03fef4a11c3756fd48f874352b1ac67c21ba112c58847ddede30bc56e2e34a20@ec2-54-164-105-7.compute-1.amazonaws.com:7739",
        'LOCATION': 'redis://127.0.0.1:6379/1',
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

LOGOUT_REDIRECT_URL = "home"
LOGIN_REDIRECT_URL = 'dashboard:admin_dashboard'
LOGIN_URL = 'auth:signin'


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get("REDISCLOUD_URL", "redis://localhost:6379")],
        },
        "ROUTING": "chat.routing.channel_routing",
    },
}

AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailBackend',  # Correct path to your custom authentication class
    'django.contrib.auth.backends.ModelBackend',  # Default Django authentication backend
]

#authentication user model
AUTH_USER_MODEL = 'accounts.User'

# CSRF_TRUSTED_ORIGINS = ['',]

