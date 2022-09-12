import os
from celery import (
    Celery
)
from celery.schedules import (
    crontab
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.beat_schedule = {
    "every-day-update_client_visit": {
        "task": "clients.tasks.update_client_visit",
        "schedule": crontab(minute=0, hour=0)
    }
}
app.autodiscover_tasks()
