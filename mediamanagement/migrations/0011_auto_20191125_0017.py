# Generated by Django 2.2.6 on 2019-11-24 18:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0010_auto_20191123_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mediamessagemodel',
            old_name='csv_file',
            new_name='vcardfile',
        ),
        migrations.AlterField(
            model_name='mediamessagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('dfefa798-0eea-11ea-8b28-645a049d591d')),
        ),
    ]
