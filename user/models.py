from django.db import models
from datetime import timedelta
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.BigIntegerField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_bot = models.BooleanField(default=False)
    is_sub = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        if self.user_name:
            return f'{self.first_name}'
        else:
            return f'{self.user_id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class KeywordCategories(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория ключевых слов'
        verbose_name_plural = 'Категории ключевых слов'

class Keyword(models.Model):
    categories = models.ForeignKey(KeywordCategories, on_delete=models.CASCADE, related_name='keywords')
    keyword = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключевые слова'


class SpamWords(models.Model):
    word = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Спам слово'
        verbose_name_plural = 'Спам слова'

class Bot(models.Model):
    name = models.CharField(max_length=255)
    bot_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'
        ordering = ['name']
    


class MessageId(models.Model):
    message_id = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return str(self.message_id)

    class Meta:
        verbose_name = 'ID сообщения'
        verbose_name_plural = 'ID сообщений'
        ordering = ['message_id']

class Message(models.Model):
    message_id = models.ForeignKey(MessageId, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'



class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    keyword = models.ForeignKey(KeywordCategories, on_delete=models.CASCADE, related_name='keyword')
    date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    duration_days = models.PositiveSmallIntegerField(default=3)  # поле для хранения длительности подписки

    @property
    def end_date(self):
        return self.date + timezone.timedelta(days=self.duration_days)  # вычисление даты окончания подписки
    
    @end_date.getter
    def end_date(self):
        return self.date + timezone.timedelta(days=self.duration_days)

    def __str__(self):
        return f'{self.user} - {self.keyword}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'keyword')


class Channels(models.Model):
    name = models.CharField(max_length=255)
    channel_id = models.BigIntegerField(unique=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'


