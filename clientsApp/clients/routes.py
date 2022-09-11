from rest_framework.routers import (
    DefaultRouter
)
from .views import (
    ClientVisitsUpdateViewSet,
    ClientViewSet
)
router = DefaultRouter()
router.register("", ClientViewSet, basename="client")
router.register("visit/update", ClientVisitsUpdateViewSet, basename="visit_update")
