from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS += [
    'gahd.net'
]

# https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/3.0/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# https://docs.djangoproject.com/en/3.0/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = True

# https://docs.djangoproject.com/en/3.0/ref/settings/#secure-hsts-seconds
SECURE_HSTS_SECONDS = 3600

# https://docs.djangoproject.com/en/3.0/ref/settings/#secure-referrer-policy
SECURE_REFERRER_POLICY = 'same-origin'

# https://docs.djangoproject.com/en/3.0/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = True

# https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/#session-cookie-secure
SESSION_COOKIE_SECURE = True

MEDIA_ROOT = str(DATA_DIR.joinpath('media'))
