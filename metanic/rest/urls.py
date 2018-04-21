from django import urls

from . import routing

routing.router.autodiscover()

urlpatterns = routing.router.urls
