# Generated by Django 2.2.6 on 2020-02-09 00:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0025_auto_20200209_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamessagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('3e7dc5de-4ad1-11ea-8400-645a049d591d')),
        ),
    ]
