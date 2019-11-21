# Generated by Django 2.2.6 on 2019-11-18 18:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messageprocess', '0010_auto_20191119_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messageprocessmodel',
            old_name='message',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='messageprocessmodel',
            old_name='to_who',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='sendingmessagemodel',
            old_name='to_who',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='messageprocessmodel',
            name='message_uuid',
            field=models.TextField(default=uuid.UUID('2b6035c0-0a33-11ea-8435-645a049d591d')),
        ),
    ]