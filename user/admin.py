from django.contrib.admin import display
from django.contrib import admin
from .models import User, Bot, Message, Subscription, Keyword, Channels, KeywordCategories, SpamWords, MessageId
from django.utils import timezone

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'user_name', 'user_id', 'date_joined','subscription_count', 'is_admin', 'is_bot','is_sub', )
    list_filter = ('is_admin', 'is_bot','is_sub',)
    search_fields = ('user_name', 'user_id', 'first_name',)

    @display(description='Количество подписок')
    def subscription_count(self, obj):
        subscription = Subscription.objects.filter(user=obj).count()
        return subscription



    
    
@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bot_id',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display  = ('id','message_id','text', 'date', )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'keyword', 'date', 'end_date', 'duration_days')


@admin.register(KeywordCategories)
class KeywordCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id','name', )
    

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('id','categories', 'keyword', )

@admin.register(SpamWords)
class SpamWordsAdmin(admin.ModelAdmin):
    list_display = ('id','word', )
    


@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'channel_id', 'date', )


@admin.register(MessageId)
class MessageIdAdmin(admin.ModelAdmin):
    list_display = ('id','message_id', )













