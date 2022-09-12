from datetime import (
    date, timedelta
)
from django.db import (
    models
)
from string import (
    digits, ascii_lowercase
)
from random import (
    choice
)


class Client(models.Model):
    """Simple Client Model"""
    name = models.CharField(
        max_length=150, verbose_name="Client name", blank=False, null=False
    )
    surname = models.CharField(
        max_length=255, verbose_name="Client surname", blank=False, null=False
    )
    email = models.EmailField(
        verbose_name="Client email", blank=True, null=True
    )
    visits = models.IntegerField(
        verbose_name="Number of client visits", default=1, blank=False, null=False
    )
    status = models.ForeignKey(
        "ClientStatus",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    active = models.BooleanField(
        default=True, verbose_name="Preempts whether the client is active"
    )
    date_joining = models.DateField(
        auto_now_add=True, verbose_name="Date of joining"
    )
    date_visit = models.DateField(
        auto_now=True, verbose_name="Date of last visit"
    )

    def __str__(self) -> str:
        return f"Client: {self.name} {self.surname}"


class ClientStatus(models.Model):
    """
    Client Status Model
    - Status directly depends on visits
    - discount depends on the status of the client
    - visits_before_receiving if clients visits == visits_before_receiving, he automatically receives a new status
    -
    """
    status = models.CharField(
        max_length=255, verbose_name="Client Status", blank=False, null=False
    )
    discount = models.IntegerField(
        verbose_name="Discount"
    )
    visits_before_receiving = models.IntegerField(
        verbose_name="Number of visits before receiving"
    )

    def __str__(self) -> str:
        return self.status


class ClientPromocode(models.Model):
    @staticmethod
    def get_promocode():
        return "".join([choice(ascii_lowercase.upper() + ascii_lowercase + digits) for _ in range(0, 6)])

    @staticmethod
    def get_date():
        return date.today() + timedelta(days=7)

    secret_number = models.CharField(
        max_length=6, default=get_promocode(), blank=False, null=False, verbose_name="Client promocode"
    )
    expiration_date = models.DateField(
        default=get_date(), verbose_name="Expiration Date", blank=False, null=False
    )
    active = models.BooleanField(
        default=True, verbose_name=""
    )
    discount = models.IntegerField(
        verbose_name="Discount"
    )
    client = models.ForeignKey(
        "Client",
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
