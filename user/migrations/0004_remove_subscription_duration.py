# Generated by Django 3.2 on 2023-02-10 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_channels_channel_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='duration',
        ),
    ]