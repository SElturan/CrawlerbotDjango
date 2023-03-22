from django.contrib.admin import display
from django.utils import timezone
from django.contrib import admin
from .models import User, Bot,Subscription, Keyword, Channels, KeywordCategories, SpamWords

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'user_name', 'user_id', 'date_joined','subscription_count', 'active_subscription_count', 'is_admin', )
    list_filter = ('is_admin','date_joined')
    list_display_links = ('id','first_name' )
    search_fields = ('user_name', 'user_id', 'first_name',)

    @display(description='Количество подписок')
    def subscription_count(self, obj):
        subscription = Subscription.objects.filter(user=obj).count()
        return subscription
    
    @display(description='Количество активных подписок')
    def active_subscription_count(self, obj):
        subscription = Subscription.objects.filter(user=obj, end_date__gte=timezone.now()).count()
        return subscription
    



    
    
@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bot_id',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'keyword', 'start_date', 'end_date', 'duration_day' )
    list_filter = ('keyword__name','start_date', 'end_date',)
    list_display_links = ('id','user', )
    search_fields = ('user__user_name', 'user__user_id', 'user__first_name', 'keyword__name')


    @display(description='Осталось дней')
    def duration_day(self, obj):
        if obj.end_date > timezone.now():
            duration_days = (obj.end_date - timezone.now()).days
        else:
            duration_days = 0
        return duration_days

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















