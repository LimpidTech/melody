import dj_database_url

from melody.settings.defaults import *

DEBUG = True

ALLOWED_HOSTS = ['services.melody.monokro.me']
FRONTEND_URL = 'melody.monokro.me'
ROOT_URLCONF = 'melody.core.urls.production'
SECRET_KEY = env_value('secret_key')
STATIC_URL = env_value('static_url')

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500),
}
