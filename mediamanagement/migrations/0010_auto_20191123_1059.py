# Generated by Django 2.2.6 on 2019-11-23 05:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0009_auto_20191123_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafilemodel',
            name='filepond',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='mediamessagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('3c2b8864-0db2-11ea-9a1e-645a049d591d')),
        ),
    ]
