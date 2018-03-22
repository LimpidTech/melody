from rest_framework import throttling


class SensitiveDataRateThrottle(throttling.AnonRateThrottle):
    scope = 'sensitive'
