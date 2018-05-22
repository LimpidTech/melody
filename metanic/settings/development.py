from metanic.settings.defaults import INSTALLED_APPS
from metanic.settings.defaults import MIDDLEWARE
from metanic.settings.defaults import REST_FRAMEWORK

from metanic.settings.defaults import cache_url
from metanic.settings.defaults import env_value
from metanic.settings.defaults import project_path 
# We specifically allow `import *` in this case to pull in expected settings
from metanic.settings.defaults import *  # noqa

ROOT_URLCONF = 'metanic.core.urls.development'

SECRET_KEY = env_value(
    'secret_key',
    'diagonal stunning powder ledge employ dealer',
)

ACCESS_CONTROL_ALLOW_ORIGINS = [
    'localhost:3030',
]

DEBUG = True
DEFAULT_FROM_EMAIL = 'services@metanic.local'
FRONTEND_URL = env_value('frontend_url', 'http://localhost:3030/')
MEDIA_ROOT = project_path('media')
MEDIA_URL = '/media/'
METANIC_REDIRECT_URL = 'http://localhost:3030/'
STATIC_ROOT = project_path('static')
STATIC_URL = '/static/'

REST_FRAMEWORK['DEFAULT_THROTTLE_CLASSES'] = []
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += (
    'rest_framework.authentication.SessionAuthentication',
)

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'anon': env_value('anon_throttle_rate', default='100/second'),
    'sensitive': env_value('sensitive_throttle_rate', default='100/second'),
    'user': env_value('user_throttle_rate', default='100/second'),
}

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

CACHES = {
    'default': cache_url('redis://localhost:6379/0'),
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': project_path(env_value('DATABASE_FILENAME', 'metanic.sqlite3')),
    },
}
ALLOWED_HOSTS = [
    'localhost',
    'metanic.local',
]

CORS_ALLOWED_ORIGINS = [
    '::1:',
    '127.0.0.1',
    '127.0.0.1:*',
    'localhost',
    'localhost:*',
    'metanic.local',
    'metanic.local:*',
]

INTERNAL_IPS = [
    '127.0.0.1',
]
