# Generated by Django 2.1.5 on 2019-01-23 12:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0012_auto_20190123_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 12, 5, 20, 417304, tzinfo=utc)),
        ),
    ]
