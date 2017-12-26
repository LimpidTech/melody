from melody.core import models


class Post(models.UUIDModel):
    subject = models.TextField()
    body = models.TextField()


class Category(models.UUIDModel):
    name = models.TextField()

    posts = models.ManyToManyField(Post, related_name='categories', blank=True)

    parent = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
