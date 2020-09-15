from rest_framework.viewsets import ModelViewSet

from .models import Patient, Hospital, Doctor, DoctorSpecialization, DoctorAppointment, Service
from .serializers import PatientModelSerializer, HospitalSerializer, DoctorSerializer, DoctorSpecializationSerializer, \
    DoctorAppointmentSerializer, ServiceSerializer


class PatientViewSet(ModelViewSet):
    serializer_class = PatientModelSerializer
    queryset = Patient.objects.all()


class HospitalViewSet(ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()


class DoctorViewSet(ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DoctorSpecializationViewSet(ModelViewSet):
    serializer_class = DoctorSpecializationSerializer
    queryset = DoctorSpecialization.objects.all()


class DoctorAppointmentViewSet(ModelViewSet):
    serializer_class = DoctorAppointmentSerializer
    queryset = DoctorAppointment.objects.all()


class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
