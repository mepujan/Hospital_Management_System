from rest_framework.routers import DefaultRouter

from .views import PatientViewSet, DoctorViewSet, DoctorAppointmentViewSet, HospitalViewSet, ServiceViewSet, \
    DoctorSpecializationViewSet

router = DefaultRouter()
router.register('patient', PatientViewSet)
router.register('doctor', DoctorViewSet)
router.register('hospital', HospitalViewSet)
router.register('doctorAppointment', DoctorAppointmentViewSet)
router.register('service', ServiceViewSet)
router.register('specialization', DoctorSpecializationViewSet)

urlpatterns = [] + router.urls
