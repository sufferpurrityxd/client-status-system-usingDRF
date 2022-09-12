import logging
from celery.utils.log import (
    get_task_logger
)
from config.celery import (
    app
)
from .models import (
    Client,
    ClientStatus,
    ClientPromocode
)
from django.db.models import (
    Q,
    F
)
from .service import (
    send_email_to_client
)
from datetime import (
    date, timedelta
)
logger = get_task_logger(__name__)


@app.task()
def update_client_status(client_id):
    """
    This task updates the client's status (if possible) when he visits the establishment
    """
    try:
        client = Client.objects.filter(
            id=client_id
        )
        for status_visits in ClientStatus.objects.filter(
            ~Q(id=client[0].status_id), visits_before_receiving__lte=client[0].visits, visits_before_receiving__gte=client[0].visits
        ):
            if status_visits.visits_before_receiving <= client[0].visits:
                client.update(
                    status=status_visits.id
                )
                if client[0].email:
                    send_email_to_client(
                        title="Congratulations you have improved your status",
                        msg="Hello {0}, you upgraded your status to {1}, now you have a {2} percent discount".format(client[0].name, client[0].status.status, client[0].status.discount),
                        client_email=client[0].email
                    )
                return True
        return False
    except Exception as ex:
        logging.info("Error!!! {0}".format(ex))


@app.task()
def promocode_to_client(client_id):
    """
    This task automatically issues promo codes to the client.
    - Imagine a system that every 30 visits the client receives a promocode for a discount(If he subscribed to the email newsletter)
    - chat is calculated by the formula client discount by status * 1.5 if his discount is more than 7 percent otherwise * 1.75
    - (I don’t care about the moments in terms of how profitable it is, I’m just trying to show how to implement this)
    """
    try:
        clients = [
            client for client in Client.objects.annotate(
                res=F('visits') % 30
            ).filter(
                res=0, active=True, email__isnull=False
            )
        ]
        [
            clients.pop(clients.index(promocode.client)) for promocode in
            ClientPromocode.objects.filter(
                client__in=clients, active=True
            ) if promocode.client in clients
        ]
        for client in clients:
            if client.status.discount > 7:
                discount = int(client.status.discount) * 2
            else:
                discount = int(client.status.discount) * 4

            promocode = ClientPromocode.objects.create(
                client=client,
                discount=discount
            )
            send_email_to_client(
                title="Congratulations, you have received a promo code",
                msg="Hello {0}, You received a promo code for a discount in {1}, Rather spend it - {2}".format(client.name, discount, promocode.secret_number),
                client_email=client.email
            )
            promocode.save()
    except Exception as ex:
        logging.info("Error!!! {0}".format(ex))


# TODO:
@app.task()
def update_client_visit():
    """
    The client becomes inactive if he has not visited our establishment for more than 30 days
    """
    try:
        Client.objects.filter(
            activte=True, date_visit=(date.today() - timedelta(days=30))
        ).update(activte=False)
        return True
    except Exception as ex:
        logging.info("Error!!! {0}".format(ex))
