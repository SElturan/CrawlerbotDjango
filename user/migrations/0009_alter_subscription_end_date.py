# Generated by Django 3.2 on 2023-02-10 15:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_subscription_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 17, 15, 51, 31, 103902, tzinfo=utc)),
        ),
    ]
