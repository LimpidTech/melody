from melody.core import models


class Post(models.UUIDModel):
    subject = models.TextField()
    body = models.TextField()
