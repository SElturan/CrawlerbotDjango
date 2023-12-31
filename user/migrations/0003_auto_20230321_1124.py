# Generated by Django 3.2 on 2023-03-21 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_subscription_duration_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='user.keywordcategories', verbose_name='Категория ключевых слов'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='keyword',
            field=models.CharField(max_length=255, unique=True, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='keywordcategories',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Наименование категории'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания подписки'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='user.keywordcategories', verbose_name='Выбранная категория'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='user.user', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='Никнейм'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Админ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.BigIntegerField(unique=True, verbose_name='ID пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Юзернейм'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='MessageId',
        ),
    ]
