from melody.settings.defaults import project_path
from melody.settings.defaults import env_value
from melody.settings.defaults import INSTALLED_APPS
from melody.settings.defaults import MIDDLEWARE

# We specifically allow `import *` in this case to pull in expected settings
from melody.settings.defaults import *  # noqa

DEBUG = True

ROOT_URLCONF = 'melody.core.urls.development'

SECRET_KEY = env_value(
    'secret_key', 'diagonal stunning powder ledge employ dealer'
)

DEFAULT_FROM_EMAIL = 'services@melody.local'
FRONTEND_URL = env_value('frontend_url', 'http://localhost:3030/')
MEDIA_ROOT = project_path('media')
MEDIA_URL = '/media/'
MELODY_REDIRECT_URL = 'http://localhost:3030/'
STATIC_ROOT = project_path('static')
STATIC_URL = '/static/'

INSTALLED_APPS += [
    'livereload',  # LiveReload needs to precede staticfiles
    'debug_toolbar',
    'django_extensions',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    'default':
        {
            'ENGINE':
                'django.db.backends.sqlite3',
            'NAME':
                project_path(env_value('DATABASE_FILENAME', 'melody.sqlite3')),
        },
}

INTERNAL_IPS = [
    '127.0.0.1',
]

CORS_ALLOWED_ORIGINS = [
    '127.0.0.1',
    '127.0.0.1:*',
    'localhost',
    'localhost:*',
    'melody.local',
    'melody.local:*',
]
