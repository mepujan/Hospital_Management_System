from ckeditor.fields import RichTextField
from django.db import models

diseases = (('Lungs Diseases', 'Lungs Diseases'), ('Heart Diseases', 'Heart Diseases'), ('Orthopaedic', 'Orthopaedic'),
            ('Dental Service', 'Dental Service'), ('Eye Care', 'Eye Care'))

gender = (('male', 'male'), ('female', 'female'), ('others', 'others'))


class DoctorSpecialization(models.Model):
    specialization = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.specialization


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=gender, default='male')
    admitted_date = models.DateField()
    checkout_date = models.DateField(default=None)
    checked_by = models.TextField()
    medicine_prescribed = models.TextField()
    profile_picture = models.ImageField(upload_to='patient', null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.email


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.hospital_name


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    specialization = models.ForeignKey(DoctorSpecialization, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=6, choices=gender, default='male')
    profile_picture = models.ImageField(upload_to='doctor', null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.email


class DoctorAppointment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    diseases = models.CharField(max_length=30, choices=diseases)
    datetime = models.DateTimeField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email


class Service(models.Model):
    service = models.CharField(max_length=100, unique=True)
    about_service = RichTextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.service
