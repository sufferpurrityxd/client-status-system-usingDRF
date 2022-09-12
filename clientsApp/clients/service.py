from config.settings import (
    EMAIL_HOST
)
from django.core.mail import (
    send_mail
)


def send_email_to_client(title, msg, client_email):
    send_mail(
        "{0}".format(title),
        "{0}".format(msg),
        EMAIL_HOST,
        client_email,
        fail_silently=False,
    )
