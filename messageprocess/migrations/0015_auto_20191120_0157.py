# Generated by Django 2.2.6 on 2019-11-19 20:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messageprocess', '0014_auto_20191119_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadCsvFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vcardfile', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='messageprocessmodel',
            name='message_uuid',
            field=models.TextField(default=uuid.UUID('0ed7b538-0b0b-11ea-a2ce-645a049d591d')),
        ),
    ]
