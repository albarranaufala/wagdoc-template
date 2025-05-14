from decouple import config

from .base import *

DEBUG = config("DEBUG", default=False, cast=bool)

SECRET_KEY = config("SECRET_KEY", default="")

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost").split(",")

try:
    from .local import *
except ImportError:
    pass
