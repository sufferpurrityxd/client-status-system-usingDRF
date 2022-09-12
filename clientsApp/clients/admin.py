from .models import (
    Client,
    ClientStatus,
    ClientPromocode
)
from django.contrib import (
    admin
)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientStatus)
class ClientStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientPromocode)
class ClientPromocodeAdmin(admin.ModelAdmin):
    pass
