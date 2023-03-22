from rest_framework import serializers
from django.utils import timezone
from .models import User, Subscription, Keyword, Channels, Bot, KeywordCategories, SpamWords



class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id','keyword', )

class KeywordCategoriesDetailSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(read_only=True, many=True)
    
    class Meta:
        model = KeywordCategories
        fields = ('id', 'name', 'keywords')




class KeywordCategoriesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeywordCategories
        fields = ('id', 'name')
        


class SubscriptionSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.user_id')
    keyword = serializers.CharField(source='keyword.name')
    
    class Meta:
        model = Subscription
        fields = ('id','user_id', 'keyword', 'start_date', 'end_date', 'duration_days' )
    
    def create(self, validated_data):
        user_id = validated_data.pop('user').get('user_id')
        user = User.objects.get(user_id=user_id)
        keyword_name = validated_data.pop('keyword').get('name')
        keyword = KeywordCategories.objects.get(name=keyword_name)
        duration_days = validated_data.pop('duration_days', 3)
        start_date = timezone.now()
        end_date = start_date + timezone.timedelta(days=duration_days)
        subscription = Subscription.objects.create(user=user, keyword=keyword, duration_days=duration_days, start_date=start_date, end_date=end_date)
        return subscription



class UserDetailSerializer(serializers.ModelSerializer):
    subscriptionserializers = SubscriptionSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id','first_name', 'user_name', 'user_id', 'is_admin',  'subscriptionserializers',)

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name', 'user_name', 'user_id', 'is_admin',)

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('id','name', 'bot_id', )


class SpamWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamWords
        fields = ('id','word', )



class ChannelsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Channels
        fields = ('id','name', 'channel_id', 'date', )


class ActiveSubscriptionSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.user_id')
    keyword = serializers.CharField(source='keyword.name')

    class Meta:
        model = Subscription
        fields = ('id','user_id', 'keyword', 'start_date', 'end_date', 'duration_days')


