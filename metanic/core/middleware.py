import functools

from django.conf import settings
from django import http
from django import urls

CORS_ALLOWED_ORIGINS = getattr(settings, 'CORS_ALLOWED_ORIGINS', [])

CORS_ALLOWED_HEADERS = getattr(
    settings, 'CORS_ALLOWED_HEADERS', [
        'Content-Type',
        'Accept',
    ]
)

CORS_ALLOWED_METHODS = getattr(
    settings, 'CORS_ALLOWED_METHODS',
    ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
)

HTTP_ORIGIN = 'HTTP_ORIGIN'
HTTP_ACR_METHOD = 'HTTP_ACCESS_CONTROL_REQUEST_METHOD'


def match(pattern, origin):
    origin_length = len(origin)
    origin_index = origin_length - 1

    if len(pattern) is 0:
        return True

    for character in reversed(pattern):
        if character == '*':
            pattern_offset = (origin_length - origin_index) * -1
            for index in range(origin_index, 0, -1):
                if match(pattern[:pattern_offset], origin[:index]):
                    return True
            return False

        if origin[origin_index] != character:
            return False

        origin_index -= 1

    return True


def origin_is_match(patterns, origin):
    for pattern in patterns:
        if match(pattern, origin):
            return True
    return False


class CORSMiddleware(object):
    """ Provides necessary responses and headers for CORS requests. """

    # TODO:
    #
    #  - Verify that this matches the spec (it probably doesn't yet :D)
    #
    #  - Consider only using this for dev. There's no reason for these requests
    #  to hit Django at all in production unless we start varying access by API
    #  resource permissions or similar.

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        method = request.META.get(HTTP_ACR_METHOD, None)

        if request.method == 'OPTIONS' and not method:
            return http.HttpResponseForbidden()

        origin = request.META.get(HTTP_ORIGIN, None)

        if origin and origin_is_match(CORS_ALLOWED_ORIGINS, origin):
            response['Access-Control-Allow-Origin'] = request.META['HTTP_ORIGIN']
            response['Access-Control-Allow-Methods'] = ",".join(CORS_ALLOWED_METHODS)
            response['Access-Control-Allow-Headers'] = ",".join(CORS_ALLOWED_HEADERS)
            response['Access-Control-Allow-Credentials'] = 'true'

        return response


def _init_extended_headers(fn):
    @functools.wraps(fn)
    def call_fn(request):
        response = fn(request)
        response.setdefault('X-Metanic-Identifier', '')
        response.setdefault('X-Metanic-IsAuthenticated', '')
        response.setdefault('X-Metanic-Username', '')
        return response
    return call_fn


class HeaderExtensionMiddleware(object):
    def __init__(self, get_response):
        self.get_response = _init_extended_headers(get_response)

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            response['X-Metanic-Identifier'] = urls.reverse('user-detail', kwargs={
                'pk': request.user.pk,
            })

        response['X-Metanic-IsAuthenticated'] = request.user.is_authenticated
        response['X-Metanic-Username'] = request.user.username

        return response
