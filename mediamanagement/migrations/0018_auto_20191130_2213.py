# Generated by Django 2.2.6 on 2019-11-30 16:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0017_auto_20191128_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamessagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('7e6aa35e-1390-11ea-b079-645a049d591d')),
        ),
    ]
