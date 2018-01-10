import dj_database_url

from melody.settings.defaults import *

DEBUG = True

ALLOWED_HOSTS = ['services.melody.monokro.me']

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500),
}
