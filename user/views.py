import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserDetailSerializer, BotSerializer,  SubscriptionSerializer, KeywordSerializer, ChannelsSerializer, KeywordCategoriesDetailSerializer, SpamWordsSerializer, ActiveSubscriptionSerializer
from .models import User, Bot, Subscription, Keyword, Channels, KeywordCategories,SpamWords



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('is_admin', 'user_id')

    
    


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('keyword__name','user__user_id',)

    def partial_update(self, request, *args, **kwargs):
        
        instance = self.get_object()
        duration_days = request.data.get('duration_days')
        if duration_days:
            instance.duration_days = duration_days
        end_date = instance.end_date + timezone.timedelta(days=instance.duration_days)
        instance.end_date = end_date
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_default(self, request):
        user_id = request.data.get('user_id')
        keyword_name = request.data.get('keyword')
        duration_days = request.data.get('duration_days', 3)
        user = User.objects.get(id=user_id)
        keyword = KeywordCategories.objects.get(name=keyword_name)
        start_date = timezone.now()
        end_date = start_date + timezone.timedelta(days=duration_days)
        subscription = Subscription.objects.create(user=user, keyword=keyword, duration_days=duration_days, start_date=start_date, end_date=end_date)
        serializer = self.get_serializer(subscription)
        return Response(serializer.data)


class ActiveSubscriptionListView(ListAPIView):
    serializer_class = ActiveSubscriptionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('keyword__name','user__user_id',)

    def get_queryset(self):
        return Subscription.objects.filter(
            end_date__gte=timezone.now(),
        ).select_related('user', 'keyword')
    

class SubscriptionExpirationListView(ListAPIView):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):


        tomorrow = timezone.now() + timezone.timedelta(days=3)
        return Subscription.objects.filter(end_date__date=tomorrow)
    # а теперь выведем всех у кого заканчивается через 3, 2 и 1 день
  

    

class BotViewSet(viewsets.ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class KeywordCategoriesViewSet(viewsets.ModelViewSet):
    queryset = KeywordCategories.objects.all()
    serializer_class = KeywordCategoriesDetailSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('name',)

    
    

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
    

    

