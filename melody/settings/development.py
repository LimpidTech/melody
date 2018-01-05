import os

from melody.settings.defaults import *

DEBUG = True

ROOT_URLCONF = 'melody.core.urls.development'
SECRET_KEY = env_value(
    'secret_key', 'diagonal stunning powder ledge employ dealer'
)

FRONTEND_URL = env_value('frontend_url', 'http://localhost:3030/')
MEDIA_ROOT = project_path('media')
MEDIA_URL = '/media/'
STATIC_ROOT = project_path('static')
STATIC_URL = '/static/'

INSTALLED_APPS += [
    'livereload',  # LiveReload needs to precede staticfiles
    'django.contrib.staticfiles',
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
