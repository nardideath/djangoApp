import os
import traceback

from django.conf import settings
from django.core.cache import cache
from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base"

    def ready(self):
        pass
