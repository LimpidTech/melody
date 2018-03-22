import dj_database_url
import os
import raven

from metanic.settings.defaults import cache_url
from metanic.settings.defaults import env_value

# We specifically allow `import *` in this case to pull in expected settings
from metanic.settings.defaults import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ['services.metanic.org']
FRONTEND_URL = 'metanic.org'
METANIC_REDIRECT_URL = 'https://metanic.org/'
ROOT_URLCONF = 'metanic.core.urls.production'
SECRET_KEY = env_value('secret_key')
STATIC_URL = env_value('static_url')

CACHES = {
    'default': cache_url(env_value('redis_url')),
}


DATABASES = {
    'default': dj_database_url.config(conn_max_age=500),
}


RAVEN_CONFIG = {
    'dsn': env_value('sentry_dsn'),
    'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}
