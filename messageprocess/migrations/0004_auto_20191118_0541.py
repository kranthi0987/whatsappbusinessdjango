# Generated by Django 2.2.7 on 2019-11-18 05:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messageprocess', '0003_auto_20191115_0448'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendingMessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('to_who', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='messageprocessmodel',
            name='message_uuid',
            field=models.TextField(default=uuid.UUID('216a4d66-09c6-11ea-b75a-c42c03361ed0')),
        ),
    ]