from django.db import models



class User(models.Model):
    first_name = models.CharField(max_length=255,verbose_name='Никнейм')
    user_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Юзернейм')
    user_id = models.BigIntegerField(unique=True, verbose_name='ID пользователя')
    is_admin = models.BooleanField(default=False, verbose_name='Админ')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')


    def __str__(self):
        if self.user_name:
            return f'{self.first_name}-{self.user_name}'
        else:
            return f'{self.user_id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class KeywordCategories(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория ключевых слов'
        verbose_name_plural = 'Категории ключевых слов'

class Keyword(models.Model):
    categories = models.ForeignKey(KeywordCategories, on_delete=models.CASCADE, related_name='keywords', verbose_name='Категория ключевых слов')
    keyword = models.CharField(max_length=255, unique=True, verbose_name='Ключевые слова')

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключевые слова'




class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='Пользователь')
    keyword = models.ForeignKey(KeywordCategories, on_delete=models.CASCADE, related_name='subscriptions', verbose_name='Выбранная категория')
    start_date = models.DateTimeField(auto_now_add= True, verbose_name='Дата подписки')
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания подписки')
    duration_days = models.IntegerField(default=3)


    def __str__(self):
        return f'({self.start_date.strftime("%d.%m.%Y")}-{self.end_date.strftime("%d.%m.%Y")})'


    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'keyword')

class Bot(models.Model):
    name = models.CharField(max_length=255)
    bot_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'
        ordering = ['name']

class Channels(models.Model):
    name = models.CharField(max_length=255)
    channel_id = models.BigIntegerField(unique=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'


class SpamWords(models.Model):
    word = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Спам слово'
        verbose_name_plural = 'Спам слова'


    