from django.contrib import admin

# Register your models here.
from messageprocess.models import MessageProcessModel, SendingMessageModel

admin.site.register(MessageProcessModel)
admin.site.register(SendingMessageModel)