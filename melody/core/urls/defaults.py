from django import urls
from django.conf import urls as legacy_urls
from django.contrib import admin

from melody.core import views

urlpatterns = [
    urls.path('admin/', admin.site.urls),
    legacy_urls.url(r'.*', views.initial),
]
