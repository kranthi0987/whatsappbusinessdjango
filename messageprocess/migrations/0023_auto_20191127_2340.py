# Generated by Django 2.2.6 on 2019-11-27 18:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messageprocess', '0022_auto_20191125_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageprocessmodel',
            name='message_uuid',
            field=models.TextField(default=uuid.UUID('2ec569f6-1141-11ea-9763-645a049d591d')),
        ),
    ]
