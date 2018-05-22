import dj_database_url
import json

from metanic.settings.defaults import cache_url
from metanic.settings.defaults import env_value

# We specifically allow `import *` in this case to pull in expected settings
from metanic.settings.defaults import *  # noqa

AWS_ACCESS_KEY_ID = env_value('AWS_ACCESS_KEY_ID')
AWS_DEFAULT_ACL = env_value('aws_default_acl', default='public-read')
AWS_S3_CUSTOM_DOMAIN = env_value('AWS_S3_CUSTOM_DOMAIN')
AWS_S3_REGION_NAME = env_value('aws_s3_region', default='us-west-1')
AWS_S3_HOST = 'metanic.media'
AWS_SECRET_ACCESS_KEY = env_value('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env_value('aws_storage_bucket_name')
DEBUG = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
FRONTEND_URL = 'metanic.org'
HSTS_ALLOW_PRELOAD = True
HSTS_INCLUDE_SUBDOMAINS = True
METANIC_REDIRECT_URL = 'https://metanic.org/'
ROOT_URLCONF = 'metanic.core.urls.production'
SECRET_KEY = env_value('secret_key')
STATIC_URL = env_value('static_url')
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

ACCESS_CONTROL_ALLOW_ORIGINS = [
    'metanic.org',
]

ALLOWED_HOSTS = [
    'metanic.services',
    'metanic-services.herokuapp.com',
]

CACHES = {
    'default': cache_url(env_value('redis_url')),
}

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500),
}

INSTALLED_APPS += [
    'storages',
]

RAVEN_CONFIG = {
    'dsn': env_value('sentry_dsn'),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },

    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'tags': {'custom-tag': 'x'},
            'class': (
                'raven.contrib.django.raven_compat'
                '.handlers.SentryHandler'
            ),
        },

        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },

    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },

        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },

        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
