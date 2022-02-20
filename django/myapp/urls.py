from rest_framework.routers import DefaultRouter

from .views import FacilityTypeViewSet, FacilityViewSet

router = DefaultRouter()
router.register('types', FacilityTypeViewSet)
router.register('facility', FacilityViewSet)


urlpatterns = router.urls
