from django.conf import settings


def global_settings(request = None):
    s = {
        "version": settings.VERSION
    }
    if request:
        s["base_url"] = "%s://%s" % (
            request.scheme,
            request.META["HTTP_HOST"]
        )
        request.global_settings = s
    return s