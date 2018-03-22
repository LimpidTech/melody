import os

from raven.contrib.django.raven_compat.models import client

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metanic.settings.production")

client.captureException()
application = get_wsgi_application()
