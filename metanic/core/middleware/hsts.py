from django.conf import settings

ONE_YEAR_IN_SECONDS = 31557600

HSTS_ALLOW_PRELOAD = getattr(settings, 'HSTS_ALLOW_PRELOAD', False)
HSTS_ENABLED = getattr(settings, 'HSTS_ENABLED', settings.DEBUG is False)
HSTS_INCLUDE_SUBDOMAINS = getattr(settings, 'HSTS_INCLUDE_SUBDOMAINS', False)
HSTS_MAX_AGE = getattr(settings, 'HSTS_MAX_AGE', ONE_YEAR_IN_SECONDS)

INITIAL_SECURITY_MODEL = 'max-age=' + str(HSTS_MAX_AGE)

class HSTSMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not HSTS_ENABLED:
            return response

        security_model = INITIAL_SECURITY_MODEL

        if HSTS_INCLUDE_SUBDOMAINS:
            security_model += '; includeSubdomains'

        if HSTS_ALLOW_PRELOAD:
            security_model += '; preload'

        response['Strict-Transport-Security'] = security_model

        return response