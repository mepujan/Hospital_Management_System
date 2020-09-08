from rest_framework.routers import DefaultRouter

from .views import PatientViewSet

router = DefaultRouter()
router.register('patient', PatientViewSet)


urlpatterns = [
                  # path('', include(router.urls)),

              ] + router.urls
