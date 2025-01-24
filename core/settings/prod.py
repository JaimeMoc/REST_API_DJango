from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "C:\Users\jaime\OneDrive\Escritorio\demo\core\settings\my.cnf",
        },
    }
}