from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
import uuid


class BaseDateTimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseDateTimeUUIDModel(BaseDateTimeModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class DbDetails(BaseDateTimeUUIDModel):
    engine = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    user = models.CharField(max_length=191)
    host = models.CharField(max_length=191)
    port = models.CharField(max_length=191)
    password = models.CharField(max_length=191)
    options = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'DbDetails:{}-{}'.format(self.uuid, self.name)


class UserDb(BaseDateTimeUUIDModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    db = models.ForeignKey(DbDetails, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'db'),)

    def __str__(self):
        return 'UserDb:{}-user({})-db({})'.format(self.uuid, self.user, self.db)
