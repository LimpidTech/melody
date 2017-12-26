import debug_toolbar

from django import urls
from django.conf import urls as legacy_urls
from django.conf import settings
from django.conf.urls import static

from melody.core.urls.defaults import urlpatterns

from melody.core import views


if settings.DEBUG is True:
    urlpatterns += [
        urls.path('/__debug/', urls.include(debug_toolbar.urls)),
        legacy_urls.url('auth/', urls.include('rest_framework.urls')),
        legacy_urls.url(r'.*', views.initial),
    ]

    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns.append(legacy_urls.url(r'.*', views.initial))
