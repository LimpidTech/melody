import uuid

from django.db.models import DateTimeField
from django.db.models import Model
from django.db.models import UUIDField

# Using `import *` here to inherit the entire Django Model interface
from django.db.models import *  # noqa


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
