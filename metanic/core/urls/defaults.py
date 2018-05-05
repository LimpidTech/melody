from django import urls
from django.contrib import admin

from metanic.collector import registration

registration.autodiscover()

urlpatterns = [
    urls.path('admin/', admin.site.urls),
]
