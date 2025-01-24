from .base import *

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "C:\\Users\\jaime\\OneDrive\\Escritorio\\demo\\core\\settings\\my.cnf",
        },
    }
}