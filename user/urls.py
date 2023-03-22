from django.urls import path

from .views import UserViewSet, BotViewSet, SubscriptionViewSet, KeywordViewSet, ChannelsViewSet, KeywordCategoriesViewSet, SpamWordsViewSet, ActiveSubscriptionListView, SubscriptionExpirationListView
app_name = "user"

urlpatterns = [
    path('user/', UserViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('user/<int:pk>/', UserViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),
    path('bot/', BotViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('bot/<int:pk>/', BotViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),

    path('subscription/', SubscriptionViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('subscription/<int:pk>/', SubscriptionViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }

    )),

    path('keywordcategories/', KeywordCategoriesViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }

    )),
    path('keywordcategories/<int:pk>/', KeywordCategoriesViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }

    )),
    
    path('keyword/', KeywordViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }

    )),

    path('keyword/<int:pk>/', KeywordViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }

    )),

    path('spamwords/', SpamWordsViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }

    )),
    path('spamwords/<int:pk>/', SpamWordsViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }

    )),
    

    path('channels/', ChannelsViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }


    )),
    path('channels/<int:pk>/', ChannelsViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }

    )),

    path('activesubscription/', ActiveSubscriptionListView.as_view()),
    path('subscriptionexpiration/', SubscriptionExpirationListView.as_view()),



]


