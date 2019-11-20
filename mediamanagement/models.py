import uuid as uuid
from django.db import models


# Create your models here.

class MediaManageModel(models.Model):
    uuid = models.TextField(default=uuid.uuid1())
    messageuuid = models.TextField(default='')
    content_type = models.TextField()
    body = models.TextField()
    file = models.FileField(blank=False, null=False)


class MediaFileModel(models.Model):
    filepond = models.FileField(blank=False, null=False)
