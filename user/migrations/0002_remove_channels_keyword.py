# Generated by Django 3.2 on 2023-02-04 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channels',
            name='keyword',
        ),
    ]
