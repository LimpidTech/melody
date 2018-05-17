from django.contrib.auth import models as auth_models
from metanic.core import models

class User(auth_models.AbstractUser, models.UUIDModel):
    """ Extend the default User model to provide UUIDs """