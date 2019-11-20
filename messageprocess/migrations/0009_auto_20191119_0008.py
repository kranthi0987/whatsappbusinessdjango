# Generated by Django 2.2.6 on 2019-11-18 18:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messageprocess', '0008_auto_20191118_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sendingmessagemodel',
            old_name='message',
            new_name='body',
        ),
        migrations.AlterField(
            model_name='messageprocessmodel',
            name='message_uuid',
            field=models.TextField(default=uuid.UUID('93970612-0a32-11ea-a557-645a049d591d')),
        ),
    ]
