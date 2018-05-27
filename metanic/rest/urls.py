from django import urls

from rest_framework_jwt import views

from . import routing

routing.router.autodiscover()

urlpatterns = routing.router.urls + [
    urls.path('jwt/obtain/', views.obtain_jwt_token),
    urls.path('jwt/verify/', views.verify_jwt_token),
]
