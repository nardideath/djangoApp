import traceback
import colorama


from django.contrib import admin
from django.utils import timezone
from django.conf import settings
from django.contrib.admin import ModelAdmin

from base.models import ShoppingBag


class ShoppingBagAdmin(ModelAdmin):
    list_display = [
        "id",
        "user",
        "quantity",
        "description",
    ]



admin.site.register(ShoppingBag, ShoppingBagAdmin)
