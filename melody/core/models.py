import uuid

from django.db.models import *


class Model(Model):
    class Meta(object):
        abstract = True

    id = None

class UUIDModel(Model):
    class Meta(object):
        abstract = True

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.pk)

