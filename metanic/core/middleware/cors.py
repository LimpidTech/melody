from django.conf import settings
from django import http
from django import urls

ACCESS_CONTROL_MAX_AGE = getattr(settings, 'ACCESS_CONTROL_MAX_AGE', 0)

ACCESS_CONTROL_ALLOW_ORIGINS = set(getattr(settings, 'ACCESS_CONTROL_ALLOW_ORIGINS', []))

ACCESS_CONTROL_ALLOW_HEADERS = set(map(str.lower, getattr(
    settings, 'ACCESS_CONTROL_ALLOW_HEADERS', [
        'Content-Type',
        'Accept',
    ]
)))

ACCESS_CONTROL_ALLOW_METHODS = set(map(str.upper, getattr(
    settings, 'ACCESS_CONTROL_ALLOW_METHODS',
    ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
)))

HTTP_ORIGIN = 'HTTP_ORIGIN'
HTTP_ACR_METHOD = 'HTTP_ACCESS_CONTROL_REQUEST_METHOD'

# This is here so that we only process the value once instead of for every request
ACCESS_CONTROL_ALLOW_METHODS_VALUE = ','.join(ACCESS_CONTROL_ALLOW_METHODS)

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
    if origin is None:
        return False

    for pattern in patterns:
        if match(pattern, origin):
            return True
    return False


class CORSMiddleware(object):
    """ Provides necessary responses and headers for CORS requests.

    The process that this implements is defined in the Cross-Origin Resource
    Sharing specification - which can be found here:

    https://www.w3.org/TR/cors/#resource-requests

    """

    def __init__(self, get_response):
        self.get_response = get_response

    def request_supports_credentials(self, request):
        """ Returns True if the given request supports credentials. Otherwise, False.

        TODO: This should actually attempt to detect credentials support

        """

        return True

    def __call__(self, request):
        response = self.get_response(request)
        origin = request.META.get(HTTP_ORIGIN, None)

        if not origin_is_match(ACCESS_CONTROL_ALLOW_ORIGINS, origin):
            # We have an Origin header, but it doesn't match ALLOW origins. Don't allow CORS here.
            return response

        response['Access-Control-Allow-Origin'] = origin

        if self.request_supports_credentials(request):
            # TODO: We should verify that the value of origin is not ` * `` here
            response['Access-Control-Allow-Credentials'] = 'true'

        if request.method != 'OPTIONS':
            response['Access-Control-Allow-Headers'] = ACCESS_CONTROL_ALLOW_HEADERS
            return response

        # At this point, we know that we have a pre-flight request
        requested_method = request.META.get(HTTP_ACR_METHOD, None)
        requested_headers = request.META.get('Access-Control-Request-Headers', [])

        if requested_method not in ACCESS_CONTROL_ALLOW_METHODS_VALUE:
            return response

        # The spec requires these to be ASCII and case-insensitive, so lower() is a safe comparison
        # in this case. Note that we intentionally don't do this above in some cases in order to
        # avoid any potential hacks using UTF-8 characters.

        if len(requested_headers) is 0:
            allowed_and_requested_header_values = ACCESS_CONTROL_ALLOW_HEADERS
        else:
            allowed_and_requested_header_values = []

            for header in requested_headers:
                if header.lower() not in ALLOW_HEADERS:
                    # Since the header isn't ALLOW, we don't allow the requested request
                    return response

                allowed_and_requested_header_values.append(header)

        response['Access-Control-Max-Age'] = ACCESS_CONTROL_MAX_AGE
        response['Access-Control-Allow-Methods'] = ACCESS_CONTROL_ALLOW_METHODS_VALUE
        response['Access-Control-Allow-Headers'] = ','.join(allowed_and_requested_header_values)

        return response