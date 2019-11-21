# Generated by Django 2.2.6 on 2019-11-19 18:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0003_auto_20191119_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mediafilemodel',
            old_name='file',
            new_name='filepond',
        ),
        migrations.AlterField(
            model_name='mediamanagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('8cedd0be-0af7-11ea-8a5a-645a049d591d')),
        ),
    ]