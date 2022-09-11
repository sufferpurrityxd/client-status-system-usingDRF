import logging
from celery.utils.log import (
    get_task_logger
)
from config.celery import (
    app
)
from .models import (
    Client,
    ClientStatus
)
from django.db.models import (
    Q
)

logger = get_task_logger(__name__)


@app.task()
def update_client_status(user_id):
    """
    This task updates the client's status (if possible) when he visits the establishment
    """
    try:
        client = Client.objects.filter(id=user_id)
        for status_visits in ClientStatus.objects.filter(
            ~Q(id=client[0].status_id), visits_before_receiving__lte=client[0].visits, visits_before_receiving__gte=client[0].visits
        ):
            if status_visits.visits_before_receiving <= client[0].visits:
                client.update(
                    status=status_visits.id
                )
                return True
        return False
    except Exception as ex:
        logging.info("Error!!! {0}".format(ex))
