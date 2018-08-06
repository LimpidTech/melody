from django.utils import text

from zope import interface

from metanic.core import models
from metanic.collector import collection

from metanic.accounts import models as accounts_models
from metanic.posts import managers
from metanic.posts import renderer


class PostTopic(models.Model):
    post_id = models.ForeignKey(
        'posts.Post',
        db_index=True,
        on_delete=models.CASCADE,
    )

    topic_id = models.ForeignKey(
        'posts.Topic',
        db_index=True,
        on_delete=models.CASCADE,
    )


class PostCategory(models.Model):
    post_id = models.ForeignKey('posts.Post', on_delete=models.DO_NOTHING)
    category_id = models.ForeignKey(
        'posts.Category', on_delete=models.DO_NOTHING
    )


@interface.implementer(collection.ICollection)
class Topic(models.CreateUpdateModel):
    class Meta(models.CreateUpdateModel.Meta):
        verbose_name_plural = 'topics'

    id = None

    name = models.TextField(unique=True)

    slug = models.SlugField(
        primary_key=True,
        blank=True,
        editable=False,
    )

    objects = managers.TopicManager()

    def __str__(self):
        return self.name

    def prepare_for_save(self):
        self.name = self.name.lower().strip()

        if not self.slug:
            self.slug = text.slugify(
                self.name,
                allow_unicode=True,
            )

    def save(self, *args, **kwargs):
        self.prepare_for_save()
        return super(Topic, self).save(*args, **kwargs)


class Category(Topic):
    class Meta(models.CreateUpdateModel.Meta):
        verbose_name_plural = 'categories'

    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # Prevents user interface issues causing infinite recursion
        if self.parent == self:
            self.parent = None

        return super(Category, self).save(*args, **kwargs)


class Post(renderer.Renderable, models.MultiSiteModel,
           models.CreateUpdateModel):
    class Meta(models.CreateUpdateModel.Meta):
        ordering = (
            '-pinned_order',
            '-created',
            '-last_modified',
        )

    subject = models.TextField()

    body = models.TextField()
    summary = models.TextField(blank=True)

    pinned_order = models.PositiveIntegerField(
        default=None,
        null=True,
        blank=True,
    )

    topics = models.ManyToManyField(
        Topic,
        related_name='posts',
        blank=True,
        editable=False,
        through=PostTopic,
    )

    categories = models.ManyToManyField(
        Category,
        related_name='categories',
        blank=True,
        editable=False,
        through=PostCategory,
    )

    author = models.ForeignKey(
        accounts_models.User,
        on_delete=models.PROTECT,
        null=True,
    )

    in_reply_to = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='replies',
    )

    def is_pinned(self):
        return self.pinned_order is not None

    def __str__(self):
        return self.subject


class History(models.CreateUpdateModel):
    post = models.ForeignKey(
        Post,
        related_name='history',
        on_delete=models.PROTECT,
    )
