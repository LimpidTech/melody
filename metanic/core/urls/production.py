from django import urls

from metanic.core.urls.defaults import urlpatterns

urlpatterns += [
    urls.path('', urls.include('metanic.rest.urls')),
]
