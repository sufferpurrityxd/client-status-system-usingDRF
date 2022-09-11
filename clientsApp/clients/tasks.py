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
from .service import (
    send_status_upgrade_email_message
)

logger = get_task_logger(__name__)


@app.task()
def update_client_status(user_id):
    """
    This task updates the client's status (if possible) when he visits the establishment
    """
    try:
        client = Client.objects.filter(
            id=user_id
        )
        for status_visits in ClientStatus.objects.filter(
            ~Q(id=client[0].status_id), visits_before_receiving__lte=client[0].visits, visits_before_receiving__gte=client[0].visits
        ):
            if status_visits.visits_before_receiving <= client[0].visits:
                client.update(
                    status=status_visits.id
                )
                if client[0].email:
                    send_status_upgrade_email_message(
                        title="Congratulations you have improved your status", msg="Hello {0}, you upgraded your status to {1}, now you have a {2} percent discount".format(
                            client[0].name, client[0].status.status, client[0].status.discount
                        ), client_email=client[0].email
                    )
                return True
        return False
    except Exception as ex:
        logging.info("Error!!! {0}".format(ex))


# TODO:
@app.task()
def update_client_visit():
    """
    The client becomes inactive if he has not visited our establishment for more than 30 days
    """
    pass
