import uuid as uuid
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.db import models


# Create your models here.
from django.utils import timezone

fs = FileSystemStorage(location='/media/storage')

class MediaMessageModel(models.Model):
    uuid = models.TextField(default=uuid.uuid1())
    content_type = models.TextField()
    filename = models.TextField()
    phone = models.TextField()
    body = models.TextField()
    caption = models.TextField()
    vcardfile = models.FileField(blank=False, null=False)
    message_date_time = models.DateTimeField(default=timezone.now)


class MediaFileModel(models.Model):
    filepond = models.FileField(blank=False, null=False)
