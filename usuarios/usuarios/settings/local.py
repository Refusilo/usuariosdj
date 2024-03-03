from .base import *
from django.core.exceptions import ImproperlyConfigured
import json
# SECURITY WARNING: don't run with debug turned on in production!
with open("secret.json") as f:
    secret=json.loads(f.read())
    
def get_secret(secret_name,secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "la variable %s no existe" %secret_name
        raise ImproperlyConfigured(msg)


DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DB_NAME"),
        'USER': get_secret("DB_USER"),
        'PASSWORD': get_secret("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL="media/"

MEDIA_ROOT= BASE_DIR / 'media'