from .models import (
    Client
)
from django.db import (
    transaction
)
from django.db.models import (
    F
)
from rest_framework import (
    serializers
)
from .tasks import (
    update_client_status
)


class ClientVisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id",)

    def update(self, instance, validated_data):
        """
        Update the number of client visits without setting a parameter
        """
        if self.instance:
            with transaction.atomic():
                client = Client.objects.filter(pk=self.instance.pk)
                client.update(visits=F('visits') + 1)
                update_client_status.delay(self.instance.pk)
                return client

    def to_representation(self, instance):
        """
        If everything went well we can enter the status
        """
        representation = super(ClientVisitsSerializer, self).to_representation(instance)
        representation['status'] = "OK"
        return representation


class ClientSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        depth = 1

    def save(self):
        """Custom save method"""
        return Client.objects.create(
            name=self.validated_data['name'],
            surname=self.validated_data['surname'],
            email=self.validated_data['email'],
            visits=self.validated_data['visits'],
            status=self.validated_data['status'],
        ).save()
