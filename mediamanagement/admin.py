from django.contrib import admin

# Register your models here.
from mediamanagement.models import MediaMessageModel, MediaFileModel

admin.site.register(MediaMessageModel)
admin.site.register(MediaFileModel)
