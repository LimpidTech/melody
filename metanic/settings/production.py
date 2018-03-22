import dj_database_url

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

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500),
}
