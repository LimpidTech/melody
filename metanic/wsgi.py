import os

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'metanic.settings.production'

print('ok ' * 100)

application = get_wsgi_application()
