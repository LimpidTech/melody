import os

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'metanic.settings.production'

application = get_wsgi_application()
