from django.db import models


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
    admitted_date = models.DateField()
    checked_by = models.TextField()
    medicine_prescribed = models.TextField()
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
    email = models.EmailField()
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    specialization = models.ForeignKey(DoctorSpecialization, on_delete=models.DO_NOTHING)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.email


