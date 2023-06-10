"""
Django settings for shushupe project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import json
import tomllib

from pathlib import Path
from dotenv import load_dotenv


# Utilities
SHUSHUPE_PACKAGE = Path(__file__).resolve().parent.parent
SHUSHUPE_PROJECT = SHUSHUPE_PACKAGE.parent

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = SHUSHUPE_PROJECT

load_dotenv(os.path.join(BASE_DIR, '.env'))
data_dir_key = 'SHUSHUPE_DATA_DIR'
DATA_DIR = Path(os.environ[data_dir_key]
                ) if data_dir_key in os.environ else BASE_DIR.parent

try:
    with DATA_DIR.joinpath('secrets.json').open() as handle:
        SECRETS = json.load(handle)
except OSError:
    SECRETS = {
        'secret_key': 'its-a-secret-to-everybody',
        'language_code': 'en-us',
        'time_zone': 'UTC'
    }

try:
    with DATA_DIR.joinpath('pyproject.toml').open() as handle:
        SHUSHUPE_TOML = tomllib.load(handle)
except OSError:
    SHUSHUPE_TOML = {
        'tool': {
            'poetry': {
                'version': '0.1.0'
            }
        }
    }

SHUSHUPE_VERSION = SHUSHUPE_TOML.get('tool').get('poetry').get('version')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(SECRETS['secret_key'])

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] + SECRETS.get('allowed_hosts', [])


# Application definition

SHUSHUPE_APPS = [
    'core.apps.CoreConfig',
    'bookmark.apps.BookmarkConfig',
    'changelog.apps.ChangelogConfig',
    'note.apps.NoteConfig',
]

EXTRA_APPS = [
    'rest_framework',
    'drf_spectacular',
]

INSTALLED_APPS = SHUSHUPE_APPS + [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + EXTRA_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.gzip.GZipMiddleware",
]

ROOT_URLCONF = 'shushupe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'shushupe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': str(SECRETS['db_engine']),
        'NAME': str(SECRETS['db_name']),
        'USER': str(SECRETS['db_user']),
        'PASSWORD': str(SECRETS['db_password']),
        'HOST': str(SECRETS['db_host']),
        'PORT': str(SECRETS['db_port']),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = str(SECRETS['time_zone'])

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


###
# https://docs.djangoproject.com/en/4.2/ref/settings/#static-files

STATIC_ROOT = str(DATA_DIR.joinpath('static'))
STATICFILES_DIRS = [str(SHUSHUPE_PACKAGE.joinpath('static')), ]

# https://docs.djangoproject.com/en/4.2/ref/settings/#media-root

MEDIA_ROOT = str(BASE_DIR.joinpath('media'))
MEDIA_URL = '/media/'

# https://docs.djangoproject.com/en/4.2/ref/settings/#login-redirect-url

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'


# Custom

SITE_NAME = str(SECRETS['site_name'])
SITE_URL = str(SECRETS['site_url'])


# Django Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

SPECTACULAR_SETTINGS = {
    'TITLE': f'{SITE_NAME} - API',
    'DESCRIPTION': f'A set of APIs of {SITE_NAME}.',
    'CONTACT': {'name': f'{SITE_NAME}', 'url': f'{SITE_URL}'},
    'VERSION': SHUSHUPE_VERSION,
    'SERVE_INCLUDE_SCHEMA': False,
}
