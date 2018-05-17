from metanic.core import models


class MailEventLogModel(models.CreateUpdateModel):
    token = models.CharField(max_length=64, db_index=True)
    raw_data = models.TextField()
