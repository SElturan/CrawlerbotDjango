# Generated by Django 3.2 on 2023-02-10 15:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20230210_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 17, 15, 16, 23, 630611, tzinfo=utc)),
        ),
    ]
