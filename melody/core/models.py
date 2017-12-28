import uuid

from django.db.models import *
from django.utils import translation


class Model(Model):
    id = None

    class Meta(object):
        abstract = True


class UUIDModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.pk)

    class Meta(object):
        abstract = True


class CreateUpdateModelMixin(Model):
    created = DateTimeField(auto_now_add=True, editable=False)
    last_modified = DateTimeField(auto_now=True, editable=False)

    class Meta(object):
        abstract = True
        ordering = ('-last_modified', '-created')
