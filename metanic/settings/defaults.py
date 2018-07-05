import datetime
import os
import urllib


def env_value(name, default=None):
    name = name.upper()
    return os.environ.get('METANIC_' + name, os.environ.get(name, default))


def project_path(*paths):
    return os.path.join(os.getcwd(), *paths)


def cache_url(url):
    parsed_url = urllib.parse.urlparse(url)
    location = parsed_url.hostname + ':' + str(parsed_url.port)

    return {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': location,
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': parsed_url.password,
        },
    }


AUTH_USER_MODEL = 'accounts.User'
DATE_FORMAT = 'Y-m-d'
DEFAULT_FROM_EMAIL = 'services@metanic.monokro.me'
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
USE_L10N = True

ACCESS_CONTROL_ALLOW_HEADERS = [
    'Accept',
    'Authorization',
    'Content-Type',
    'Cookie',
]

ACCESS_CONTROL_EXPOSE_HEADERS = [
    # Authentication headers
    'X-Metanic-IsAuthenticated',
    'X-Metanic-Username',
    'X-Metanic-Identifier',
]

ACCESS_CONTROL_ALLOW_ORIGINS = [
    'https://metanic.org',
]

ANYMAIL = {
    'MAILGUN_SENDER_DOMAIN': 'metanic.local',
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgiref.inmemory.ChannelLayer',
        'ROUTING': 'metanic.realtime.routing.routes',
    }
}

COLLECTION_SERIALIZER_TYPES = {
    'post': ('metanic.posts.api.serializers', 'PostSerializer'),
}

PLUGIN_MODULES = env_value('plugin_modules', default='')

if PLUGIN_MODULES == 'auto':
    # TODO: Automatically detect plugins based on module names.
    PLUGIN_MODULES = []

else:
    PLUGIN_MODULES = list(filter(None, PLUGIN_MODULES.split(',')))

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'anymail',
    'channels',
    'raven.contrib.django.raven_compat',
    'rest_framework',

    'metanic.accounts',
    'metanic.collector',
    'metanic.core',
    'metanic.mail',
    'metanic.posts',
    'metanic.realtime',
    'metanic.multisite',

# This lets you add METANIC_PLUGIN_MODULES to your environment to add
# additional functionality without forking Metanic.
] + PLUGIN_MODULES

INTERNAL_IPS = []

MIDDLEWARE = [
    'metanic.core.middleware.MultiSiteMiddleware',
    'metanic.core.middleware.CORSMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'metanic.core.middleware.HSTSMiddleware',
    'metanic.core.middleware.AuthenticationHeadersMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'metanic.accounts.authentication.CSRFExemptAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],

    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],

    'DEFAULT_THROTTLE_RATES': {
        'anon': env_value('anon_throttle_rate', default='1000/second'),
        'sensitive': env_value('sensitive_throttle_rate', default='3/second'),
        'user': env_value('user_throttle_rate', default='10000/second'),
    },
}

TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'metanic.core.context_processors.frontend_url',
            ],
        }
    },
]

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=14),
}