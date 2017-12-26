import debug_toolbar

from django import urls
from django.conf import settings
from django.conf.urls import static

from melody.core.urls.defaults import urlpatterns


if settings.DEBUG is True:
    urlpatterns += [
        urls.path('/__debug/', urls.include(debug_toolbar.urls)),
    ]

    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
