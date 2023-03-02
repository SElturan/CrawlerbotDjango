from rest_framework import serializers

from .models import User, Message, Subscription, Keyword, Channels, Bot, KeywordCategories, SpamWords, MessageId



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
        fields = ('id', 'user_id', 'keyword', 'date', 'end_date', 'duration_days')
    
    def create(self, validated_data):
        user_id = validated_data.pop('user').get('user_id')
        user = User.objects.get(user_id=user_id)
        keyword_name = validated_data.pop('keyword').get('name')
        keyword = KeywordCategories.objects.get(name=keyword_name)
        subscription = Subscription.objects.create(user=user, keyword=keyword, **validated_data)
        return subscription
    


class UserDetailSerializer(serializers.ModelSerializer):
    subscriptionserializers = SubscriptionSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id','first_name', 'user_name', 'user_id', 'is_admin', 'is_bot','is_sub', 'subscriptionserializers',)

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name', 'user_name', 'user_id', 'is_admin', 'is_bot','is_sub',)

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('id','name', 'bot_id', )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id','message_id','text', 'date', )

class MessageIdDetailSerializer(serializers.ModelSerializer):
    message = MessageSerializer(read_only = True, many = True)
    class Meta:
        model = MessageId
        fields = ('id','message_id', 'message' )

class MessageIdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageId
        fields = ('id','message_id', )


class SpamWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamWords
        fields = ('id','word', )









class ChannelsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Channels
        fields = ('id','name', 'channel_id', 'date', )



