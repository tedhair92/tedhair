from django.db import models

# Create your models here.


class UserDetail(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateTimeField()
    PhoneNumber = models.CharField(max_length=30)
    email = models.EmailField()
    ssn = models.CharField(max_length=30)
    page1 = models.FileField(upload_to='DriversLicense/%Y/%m/%d')
    page2 = models.FileField(upload_to='DriversLicense/%Y/%m/%d')
    UtilityBill = models.FileField(upload_to='utility/%Y/%m/%d')


class applicant(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateTimeField()
    PhoneNumber = models.CharField(max_length=30)
    email = models.EmailField()
    ssn = models.CharField(max_length=30)
    page1 = models.FileField(upload_to='DriversLicense/%Y/%m/%d')
    page2 = models.FileField(upload_to='DriversLicense/%Y/%m/%d')
    UtilityBill = models.FileField(upload_to='utility/%Y/%m/%d')
