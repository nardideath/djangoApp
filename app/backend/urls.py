import os

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = "Admin v. %s" % settings.VERSION
admin.site.site_title = "Admin v. %s" % settings.VERSION
admin.site.site_url = ""
admin.site.index_title = "Admin v. %s" % settings.VERSION

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('', include("base.urls")),
]


# AAA: Static files works only on debug true
urlpatterns += static(
    "/internal_media/",
    document_root= os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
            "../internal_media"
        )
    )
)

urlpatterns += static(
    "/media/",
    document_root=settings.MEDIA_ROOT
)

urlpatterns += staticfiles_urlpatterns()

