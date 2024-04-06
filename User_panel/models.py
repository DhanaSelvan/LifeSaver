from django.db import models

# Create your models here.
class LoginDetails(models.Model):
    Username = models.CharField(max_length=30,default="")
    EmailId = models.CharField(max_length=30,default="")
    Phonenumber = models.CharField(max_length=20,default="")
    Password = models.CharField(max_length=30,default="")
    ConformPassword = models.CharField(max_length=30,default="")
    
class DonorDetails(models.Model):
    Fullname = models.CharField(max_length=30,default="")
    EmailId = models.CharField(max_length=30,default="")
    Gender = models.CharField(max_length=10, default="")
    BloodGroup = models.CharField(max_length=30,default="")
    DOB = models.CharField(max_length=10, default="")
    State = models.CharField(max_length=30,default="")
    District = models.CharField(max_length=30,default="")
    Address = models.CharField(max_length=100,default="")
    Contact = models.CharField(max_length=20,default="")
    # Photo = models.ImageField(default="") 

class RequestDetails(models.Model):
    UserName = models.CharField(max_length=30,default="")
    UserPhoneNumber = models.CharField(default=(""), max_length=20)
    Patient_Name = models.CharField(max_length=30, default="")
    Attender_contact_number = models.CharField(max_length=30, default="")
    Blood_Group = models.CharField(max_length=30, default="")
    Units = models.IntegerField(default="")
    Reason = models.CharField(max_length=30, default="")
    State = models.CharField(max_length=30, default="")
    City = models.CharField(max_length=30, default="")
    Hospital = models.CharField(max_length=150, default="")
    
class BloodCampDetails(models.Model):
    OrganiserName = models.CharField(max_length=50, default="")
    ContactNumber = models.CharField(max_length=10, default="")
    Venue = models.CharField(max_length=100, default="")
    Date = models.CharField(max_length=10, default="")
    Time = models.CharField(max_length=20,default="")