# Generated by Django 2.2.6 on 2019-11-14 17:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messageprocess', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageprocessmodel',
            name='uuid',
        ),
        migrations.AddField(
            model_name='messageprocessmodel',
            name='message_uuid',
            field=models.TextField(default=uuid.UUID('a538c534-0703-11ea-bb5b-645a049d591d')),
        ),
    ]