from django.contrib import admin

from .models import Patient, DoctorSpecialization, Doctor, Hospital, DoctorAppointment, Service

admin.site.register(Patient)
admin.site.register(DoctorSpecialization),
admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(DoctorAppointment)
admin.site.register(Service)
