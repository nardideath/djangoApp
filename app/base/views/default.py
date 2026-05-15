from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    context = {
        "request": request,
        "title": "My home page",
        "message": "My message"
    }

    if request.META["HTTP_USER_AGENT"].lower().find("win64") > -1:
        context["windows"] = True

    return render(request, "index.html", context)


def items(request):
    context = {
        "request": request,
        "title": "ShoppingBag Items",
    }

    if request.META["HTTP_USER_AGENT"].lower().find("win64") > -1:
        context["windows"] = True

    return render(request, "items.html", context)


def contacts(request):
    return render(request, "contacts.html")