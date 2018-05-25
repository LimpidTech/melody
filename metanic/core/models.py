import uuid

from django.db import models

# Using `import *` here to inherit the entire Django Model interface
from django.db.models import *  # noqa


class Model(models.Model):
    """ By default, our Models don't have IDs because they're often unnecessary.

    """

    id = None

    class Meta(object):
        abstract = True


class UUIDModel(models.Model):
    """ Model providing UUIDs """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(Model.Meta):
        abstract = True

    def __str__(self):
        return str(self.pk)


class CreateUpdateModel(UUIDModel):
    """ Model providing UUIDs and create/update timings. """

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta(UUIDModel.Meta):
        abstract = True
        ordering = ('-last_modified', '-created')
