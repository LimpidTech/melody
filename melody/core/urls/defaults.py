from django import urls
from django.contrib import admin

from melody.collector import registration

registration.autodiscover()

urlpatterns = [
    urls.path('admin/', admin.site.urls),
    urls.path('services/', urls.include('melody.rest.urls'))
]
