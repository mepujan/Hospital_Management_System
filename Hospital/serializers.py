from rest_framework import serializers

from .models import Patient, Hospital, Doctor, DoctorSpecialization, DoctorAppointment, Service


class PatientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class DoctorSpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSpecialization
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAppointment
        fields = '__all__'
