# Generated by Django 2.2.6 on 2020-02-09 00:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mediamanagement', '0030_auto_20200209_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamessagemodel',
            name='uuid',
            field=models.TextField(default=uuid.UUID('da50351a-4ad3-11ea-936d-645a049d591d')),
        ),
    ]
