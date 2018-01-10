from django.contrib.auth import models as auth_models
from zope import interface

from melody.core import models
from melody.collector import collection

from melody.posts import renderer


class Post(models.CreateUpdateModelMixin, models.UUIDModel, renderer.Renderable):
    subject = models.TextField()
    body = models.TextField()

    author = models.ForeignKey(
        auth_models.User,
        on_delete=models.PROTECT,
        null=True,
    )

    in_reply_to = models.ForeignKey(
        'self',
        related_name='replies',
        on_delete=models.PROTECT,
    )

    class Meta(object):
        ordering = ('in_reply_to',) + models.CreateUpdateModelMixin.Meta.ordering

class History(models.CreateUpdateModelMixin, models.UUIDModel):
    post = models.ForeignKey(
        Post,
        related_name='history',
        on_delete=models.PROTECT,
    )

    class Meta(object):
        ordering = ('post', models.CreateUpdateModelMixin.Meta.ordering)


@interface.implementer(collection.ICollection)
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
        on_delete=models.PROTECT,
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
