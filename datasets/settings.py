"""
Django settings for datasets project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hpc+78hkkwjxly-62&5)gy*1nfe9vaz3&5zeqqw7q&9_1zyr*7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
    'rest_framework',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

ROOT_URLCONF = 'datasets.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = {
    "base.auth.KeycloakOIDCAuthenticationBackend",

}

OIDC_RP_CLIENT_ID = 'datasets'
OIDC_RP_CLIENT_SECRET = '808f7d8b-c3ff-40f1-a0bc-cc05b88c3bae'
OIDC_KEYCLOAK_REALM = os.environ.get("OIDC_KEYCLOAK_REALM",
                                     "http://localhost:8080/auth/realms/myrealm/")

# OIDC_OP_AUTHORIZATION_ENDPOINT = "<URL of the OIDC OP authorization endpoint>"
OIDC_OP_AUTHORIZATION_ENDPOINT = os.path.join(OIDC_KEYCLOAK_REALM, "protocol/openid-connect/auth")
# OIDC_OP_TOKEN_ENDPOINT = "<URL of the OIDC OP token endpoint>"
OIDC_OP_TOKEN_ENDPOINT = os.path.join(OIDC_KEYCLOAK_REALM, "protocol/openid-connect/token")
# OIDC_OP_USER_ENDPOINT = "<URL of the OIDC OP userinfo endpoint>"
OIDC_OP_USER_ENDPOINT = os.path.join(OIDC_KEYCLOAK_REALM, "protocol/openid-connect/userinfo")
# OIDC_OP_JWKS_ENDPOINT = "<URL of the OIDC OP certs endpoint>" - This is required when using RS256.
OIDC_OP_JWKS_ENDPOINT = os.path.join(OIDC_KEYCLOAK_REALM, "protocol/openid-connect/certs")
# OIDC_OP_LOGOUT_ENDPOINT = "<URL of the OIDC OP certs endpoint>" - This is required when using RS256.
OIDC_OP_LOGOUT_ENDPOINT = os.path.join(OIDC_KEYCLOAK_REALM, "protocol/openid-connect/logout")

# Override method to also log user out from Keycloak as well as Django.
# If desired, this should be set to "fragalysis.views.keycloak_logout"
OIDC_OP_LOGOUT_URL_METHOD = os.environ.get("OIDC_OP_LOGOUT_URL_METHOD")

# LOGIN_REDIRECT_URL = "<URL path to redirect to after login>"
LOGIN_REDIRECT_URL = "/viewer/react/landing"
# LOGOUT_REDIRECT_URL = "<URL path to redirect to after logout - must be in keycloak call back if used>"
LOGOUT_REDIRECT_URL = "/viewer/react/landing"

# After much trial and error
# Using RS256 + JWKS Endpoint seems to work with no value for OIDC_RP_IDP_SIGN_KEY seems to work for authentication.
# Trying HS256 produces a "JWS token verification failed" error for some reason.
OIDC_RP_SIGN_ALGO = "RS256"

WSGI_APPLICATION = 'datasets.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

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
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
