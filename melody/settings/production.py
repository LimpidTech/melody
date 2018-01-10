import dj_database_url

from melody.settings.defaults import *

DEBUG = True

ALLOWED_HOSTS = ['services.melody.monokro.me']
ROOT_URLCONF = 'melody.core.urls.production'
SECRET_KEY = env_value('secret_key')

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500),
}
