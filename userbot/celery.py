# celery.py


import os
from celery import Celery
from celery.schedules import crontab

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userbot.settings')
app = Celery('user', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_notification': {
        'task': 'user.tasks.send_notification',
        'schedule': 10.0,
    },

}
