# Generated by Django 2.0.6 on 2018-06-23 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180623_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 23, 14, 48, 1, 114253)),
        ),
    ]
