from django.db import models

# Create your models here.
from django.utils import timezone
import uuid


class MessageProcessModel(models.Model):
    message_uuid = models.TextField(default=uuid.uuid1())
    from_who = models.TextField()
    phone = models.TextField()
    body = models.TextField()
    sent_status = models.BooleanField()
    message_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message_uuid


class SendingMessageModel(models.Model):
    body = models.TextField()
    phone = models.TextField()

    def __str__(self):
        return self.body


class ReadCsvFileModel(models.Model):
    vcardfile = models.FileField(blank=False, null=False)
    body = models.TextField(default='')
    phone = models.TextField(default='')
