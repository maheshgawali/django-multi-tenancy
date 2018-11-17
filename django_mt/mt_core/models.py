from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
import uuid

MAX_LENGTH = 191


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
    engine = models.CharField(max_length=MAX_LENGTH)
    name = models.CharField(max_length=MAX_LENGTH)
    user = models.CharField(max_length=MAX_LENGTH)
    host = models.CharField(max_length=MAX_LENGTH)
    port = models.IntegerField()
    password = models.CharField(max_length=MAX_LENGTH)
    options = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'DbDetails:{}-{}'.format(self.uuid, self.name)


class DomainDb(BaseDateTimeUUIDModel):
    name = models.CharField(max_length=MAX_LENGTH)
    db = models.ForeignKey(DbDetails, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'db'),)

    def __str__(self):
        return 'UserDb:{}-user({})-db({})'.format(self.uuid, self.name, self.db)
