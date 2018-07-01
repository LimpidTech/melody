import functools

from django import urls


def _init_extended_headers(fn):
    @functools.wraps(fn)
    def call_fn(request):
        response = fn(request)
        response.setdefault('X-Metanic-Identifier', '')
        response.setdefault('X-Metanic-IsAuthenticated', '')
        response.setdefault('X-Metanic-Username', '')
        return response
    return call_fn


class AuthenticationHeadersMiddleware(object):
    def __init__(self, get_response):
        self.get_response = _init_extended_headers(get_response)

    def __call__(self, request):
        response = self.get_response(request)

        if request.method == 'OPTIONS':
            return response

        # Need to update request.user here, but django-restframework-jwt doesn't
        # do this for us. Yay! :'(
        if request.user.is_authenticated:
            response['X-Metanic-Identifier'] = urls.reverse('user-detail', kwargs={
                'pk': request.user.pk,
            })

        response['X-Metanic-IsAuthenticated'] = request.user.is_authenticated
        response['X-Metanic-Username'] = request.user.username

        return response
