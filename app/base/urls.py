from django.urls import include, path, re_path
from django.conf import settings
from django.contrib import admin


import base.views as base_views


base_view_list = [
    path(
        "",
        base_views.index,
        name="index"
    ),
    path(
        "contacts/",
        base_views.contacts,
        name="contacts"
    ),
    path(
        "items/",
        base_views.items,
        name="items"
    ),
]


urlpatterns = base_view_list