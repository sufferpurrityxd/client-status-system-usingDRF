from rest_framework.viewsets import (
    GenericViewSet
)
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin
)
from .serializers import (
    ClientVisitsSerializer,
    ClientSerailizer,
    ClientPromocodeActiveSerializer,
    ClientReviewSerailizer
)
from .models import (
    Client,
    ClientStatus,
    ClientPromocode,
    ClientReview,
    
)
from rest_framework.filters import (
    OrderingFilter
)
from django_filters import (
    rest_framework as filters
)
from rest_framework.permissions import (
    IsAdminUser,
)
from .filtersets import (
    ClientFilterSet
)


class ClientVisitsUpdateViewSet(UpdateModelMixin,
                                GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientVisitsSerializer
    # permission_classes = (IsAdminUser,)  # Needs JWT tokens

class ClientViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    ListModelMixin,
                    GenericViewSet
                    ):
    queryset = Client.objects.all()
    serializer_class = ClientSerailizer
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend)
    filterset_class = ClientFilterSet
    ordering_fields = ('visits', 'date_joining', 'date_visit')
    # permission_classes = (IsAdminUser,)  # Needs JWT tokens

    def perform_create(self, serializer):
        """
        We get the client status depending on how many visits he had before registering in the system
        """
        serializer.validated_data['status'] = ClientStatus.objects.get(visits_before_receiving__lte=serializer.validated_data['visits'])
        serializer.save()


class ClientPromocodeActiveUpdateViewSet(UpdateModelMixin,
                                         GenericViewSet):
    queryset = ClientPromocode.objects.all()
    serializer_class = ClientPromocodeActiveSerializer
    # permission_classes = (IsAdminUser,)  # Needs JWT tokens


class ClientReviewViewSet(CreateModelMixin,
                          RetrieveModelMixin,
                          UpdateModelMixin,
                          DestroyModelMixin,
                          ListModelMixin,
                          GenericViewSet
                        ):
    queryset = ClientReview.objects.all()
    serializer_class = ClientReviewSerailizer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("rating",)
    

