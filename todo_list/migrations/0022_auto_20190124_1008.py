# Generated by Django 2.1.5 on 2019-01-24 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0021_auto_20190124_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='updated_at',
            field=models.DateTimeField(default=None),
        ),
    ]
