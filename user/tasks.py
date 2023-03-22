from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import Subscription
import requests

@shared_task
def send_notification():
    print('Sending notifications...')
    print('test')
    
    subscriptions = Subscription.objects.filter(end_date__date=timezone.now() + timedelta(days=3))
    for subscription in subscriptions:
       
        remaining_days = (subscription.end_date - timezone.now()).days
        
        message = f'Подписка на категорию "{subscription.keyword}" закончится через {remaining_days} дня. Не забудьте оплатить.'

        bot_url = 'https://api.telegram.org/bot5900825746:AAHJ4dHDHKMDVvv-foLVtzH6TSFpLju5BmQ/sendMessage'
        data = {
            'chat_id': subscription.user.user_id,
            'text': message
        }
        print(data)
        response = requests.post(bot_url, data=data)
        if response.status_code == 200:
            
            subscription.notified = True
            subscription.save()

