from django.conf import settings


class ContentSecurityPolicyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def get_policy(self):
        """ Get value for the Content-Security-Policy header. """

        # TODO: Use settings for this after some thought about how to
        #       maintain best performance.

        return (
            'default-src htts://metanic.services; '
            'img-src https://metanic.media; '
            'media-src https://metanic.media; '
            'script-src https://metanic.media; '
            'style-src https://metanic.media; '
            'report-uri https://metsanic.services/security_policie_report/; '
        )

    def __call__(self, request):
        response = self.get_response(request)
        response['Content-Security-Policy'] = self.get_policy()
        return response
