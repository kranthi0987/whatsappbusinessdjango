from django.db import models

# Create your models here.
from django.utils import timezone
import uuid
from django.db import models


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


class MessageCounter(models.Model):
    text_message_count = models.BigIntegerField(default=0)


class MessageListModel(models.Model):
    message_uuid = models.TextField(default=uuid.uuid1())
    from_whom = models.TextField(blank=True, null=True)
    to_whom = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    message_type = models.TextField(blank=True, null=True)
    file_url = models.TextField(blank=True, null=True)
    content_type = models.TextField(blank=True, null=True)
    sent_status = models.TextField(blank=True, null=True)
    message_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message_uuid