# Generated by Django 2.2.6 on 2019-12-01 05:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0020_auto_20191201_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamessagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('3df9624a-13fe-11ea-8e64-645a049d591d')),
        ),
    ]