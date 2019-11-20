from django.contrib import admin

# Register your models here.
from mediamanagement.models import MediaManageModel, MediaFileModel

admin.site.register(MediaManageModel)
admin.site.register(MediaFileModel)
