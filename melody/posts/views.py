import os

from django import template
from django import shortcuts

from . import models


def get_template_path(*args):
    return os.path.join('posts', *args)


def posts_list(request):
    return shortcuts.render(request, get_template_path('posts_list.html'), {
        'request': request,
        'posts': models.Post.objects.all(),
    }, content_type='text/html')
