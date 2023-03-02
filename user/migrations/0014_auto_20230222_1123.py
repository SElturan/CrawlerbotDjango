# Generated by Django 3.2 on 2023-02-22 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_subscription_subscription_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.BigIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'ID сообщения',
                'verbose_name_plural': 'ID сообщений',
                'ordering': ['message_id'],
            },
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='subscription_end_date',
        ),
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='user.messageid'),
        ),
    ]