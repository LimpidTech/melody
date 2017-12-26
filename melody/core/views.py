import os

from django import template
from django import shortcuts


def get_template_path(*args):
    return os.path.join(*args)


def initial(request):
    return shortcuts.render(
        request,
        get_template_path('core', 'base.html'),
        content_type='text/html',
    )
