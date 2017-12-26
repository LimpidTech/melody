import os

from melody.settings.defaults import *

DEBUG = True

ROOT_URLCONF = 'melody.core.urls.development'
SECRET_KEY = env_value('secret_key', 'diagonal stunning powder ledge employ dealer')

STATIC_URL = '/static/'
STATIC_ROOT = project_path('static')

MEDIA_URL = '/media/'
MEDIA_ROOT = project_path('media')

INSTALLED_APPS += [
    'django.contrib.staticfiles',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# settings.py
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': project_path(env_value('DATABASE_FILENAME', 'melody.sqlite3')),
  }
}

