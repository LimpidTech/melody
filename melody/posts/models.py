from django.contrib.auth import models as auth_models
from zope.interface import implementer

from melody.core import models

from . import collection


class Post(models.CreateUpdateModelMixin,  models.UUIDModel):
    subject = models.TextField()
    body = models.TextField()

    author = models.ForeignKey(
        auth_models.User,
        on_delete=models.SET_NULL,
        null=True,
    )


@implementer(collection.Collection)
class Topic(models.CreateUpdateModelMixin, models.UUIDModel):
    name = models.TextField()

    posts = models.ManyToManyField(
        Post,
        related_name='categories',
        blank=True,
        editable=False,
    )

    class Meta(object):
        verbose_name_plural = 'categories'


@implementer(collection.Collection)
class Category(Topic):
    parent = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.parent == self:
            self.parent = None

        return super(Category, self).save(*args, **kwargs)

    class Meta(object):
        verbose_name_plural = 'categories'
