import os
from .base import *  # noqa: F401, F403

SECRET_KEY = "Cu96ky2qXk9yxxd4CrDOlQpFrCTJNl31sxtxBhEfpVBDxe6SGOlkUUuFT7nqk654"

SITE_ID = 3
ALLOWED_HOSTS = ["*"]
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "hello_django_ci",
        "USER": "hello_django",
        "PASSWORD": "hello_django",
        "HOST": "postgres",
        "PORT": "5432",
    }
}
