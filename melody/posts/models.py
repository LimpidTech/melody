from django.contrib.auth import models as auth_models
from zope.interface import implementer

from melody.core import models

from melody.collector import collection


class Post(models.CreateUpdateModelMixin, models.UUIDModel):
    subject = models.TextField()
    body = models.TextField()

    author = models.ForeignKey(
        auth_models.User,
        on_delete=models.SET_NULL,
        null=True,
    )


@implementer(collection.ICollection)
class Topic(models.CreateUpdateModelMixin, models.UUIDModel):
    name = models.TextField(unique=True)

    posts = models.ManyToManyField(
        Post,
        related_name='topics',
        blank=True,
        editable=False,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower().strip()
        return super(Topic, self).save(*args, **kwargs)

    class Meta(models.CreateUpdateModelMixin.Meta):
        verbose_name_plural = 'topics'


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

    class Meta(models.CreateUpdateModelMixin.Meta):
        verbose_name_plural = 'categories'

        ordering = ('parent',) + models.CreateUpdateModelMixin.Meta.ordering
