# Generated by Django 2.1.5 on 2019-01-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0024_auto_20190124_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='item',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
