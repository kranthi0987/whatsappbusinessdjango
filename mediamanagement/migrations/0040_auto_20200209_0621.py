# Generated by Django 2.2.6 on 2020-02-09 00:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0039_auto_20200209_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamessagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('4803f4fa-4ad6-11ea-bc12-645a049d591d')),
        ),
    ]
