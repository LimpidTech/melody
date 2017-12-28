from zope.interface import implements

from melody.core import models

from . import collections


class Post(models.CreateUpdateModelMixin,  models.UUIDModel):
    subject = models.TextField()
    body = models.TextField()


class Category(models.CreateUpdateModelMixin, models.UUIDModel):
    implements(collections.Collection)

    class Meta(object):
        verbose_name_plural = 'categories'

    name = models.TextField()

    posts = models.ManyToManyField(
        Post,
        related_name='categories',
        blank=True,
        editable=False,
    )

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
