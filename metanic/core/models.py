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


class UUIDModelMixin(object):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.pk)


class UUIDModel(UUIDModelMixin, Model):
    """ Model providing UUIDs """

    class Meta(object):
        abstract = True


class CreateUpdateModelMixin(object):
    created = DateTimeField(auto_now_add=True, editable=False)
    last_modified = DateTimeField(auto_now=True, editable=False)

    class Meta(object):
        ordering = ('-last_modified', '-created')


class CreateUpdateModel(CreateUpdateModelMixin, UUIDModel):
    """ Model providing UUIDs and create/update timings. """

    # TODO: Django apparently requires this. The Mixin doesn't add them. Something silly going on.
    id = UUIDModelMixin.id
    created = CreateUpdateModelMixin.created
    last_modified = CreateUpdateModelMixin.last_modified

    class Meta(CreateUpdateModelMixin.Meta):
        abstract = True