from rest_framework.routers import (
    DefaultRouter
)
from .views import (
    ClientVisitsUpdateViewSet,
    ClientPromocodeActiveUpdateViewSet,
    ClientViewSet,
    ClientReviewViewSet
)
router = DefaultRouter()
router.register("", ClientViewSet, basename="client")
router.register("visit/update", ClientVisitsUpdateViewSet, basename="visit_update")
router.register("promocode/update", ClientPromocodeActiveUpdateViewSet, basename="promocode_update")
router.register("review", ClientReviewViewSet, basename="review")
