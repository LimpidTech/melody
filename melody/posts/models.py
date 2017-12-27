from melody.core import models


class Post(models.CreateUpdateModelMixin,  models.UUIDModel):
    subject = models.TextField()
    body = models.TextField()


class Category(models.CreateUpdateModelMixin, models.UUIDModel):
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
