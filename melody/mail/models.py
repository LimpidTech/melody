from melody.core import models


class MailEventLogModel(models.CreateUpdateModelMixin, models.UUIDModel):
    token = models.CharField(max_length=64, db_index=True)
    raw_data = models.TextField()
