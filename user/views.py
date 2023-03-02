import django_filters.rest_framework
from rest_framework import viewsets
from .serializers import UserDetailSerializer, BotSerializer, MessageSerializer, SubscriptionSerializer, KeywordSerializer, ChannelsSerializer, KeywordCategoriesDetailSerializer, SpamWordsSerializer, MessageIdDetailSerializer
from .models import User, Bot, Message, Subscription, Keyword, Channels, KeywordCategories,SpamWords, MessageId





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('is_admin', 'user_id', 'is_sub')



class BotViewSet(viewsets.ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class MessageIdViewSet(viewsets.ModelViewSet):
    queryset = MessageId.objects.all()
    serializer_class = MessageIdDetailSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('user__user_id',)


class KeywordCategoriesViewSet(viewsets.ModelViewSet):
    queryset = KeywordCategories.objects.all()
    serializer_class = KeywordCategoriesDetailSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

class SpamWordsViewSet(viewsets.ModelViewSet):
    queryset = SpamWords.objects.all()
    serializer_class = SpamWordsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)



class ChannelsViewSet(viewsets.ModelViewSet):
    queryset = Channels.objects.all()
    serializer_class = ChannelsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
