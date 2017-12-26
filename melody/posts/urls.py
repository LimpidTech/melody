from django import urls

from . import views

urlpatterns = [
    urls.path('', views.posts_list)
]
