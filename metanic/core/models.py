import uuid

from django.db.models import DateTimeField
from django.db.models import Model
from django.db.models import UUIDField

# Using `import *` here to inherit the entire Django Model interface
from django.db.models import *  # noqa


class Model(Model):
    """ By default, our Models don't have IDs because they're often unnecessary.
    
    """

    id = None

    class Meta(object):
        abstract = True


class UUIDModel(Model):
    """ Model providing UUIDs """

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(Model.Meta):
        abstract = True

    def __str__(self):
        return str(self.pk)


class CreateUpdateModel(UUIDModel):
    """ Model providing UUIDs and create/update timings. """

    created = DateTimeField(auto_now_add=True, editable=False)
    last_modified = DateTimeField(auto_now=True, editable=False)

    class Meta(UUIDModel.Meta):
        ordering = ('-last_modified', '-created')
