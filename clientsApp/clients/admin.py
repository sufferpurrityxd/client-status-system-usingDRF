from .models import (
    Client,
    ClientStatus
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
