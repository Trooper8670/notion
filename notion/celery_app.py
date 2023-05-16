import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notion.settings')

celery = Celery('notion')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.autodiscover_tasks()

@celery.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
