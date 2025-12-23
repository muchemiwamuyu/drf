from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class SchoolAdmin(models.Model):
    platformDeveloper = models.OneToOneField(User, on_delete=models.CASCADE)
    groupCategory = models.OneToOneField(Group, default=None, on_delete=models.CASCADE, null=True, blank=True)
    fullName = models.CharField(max_length=255, null=True)
    schoolName = models.CharField(max_length=255)
    schoolAddress = models.CharField(max_length=255)
    contactNumber = models.IntegerField()
    emailAddress = models.EmailField()

    def __str__(self):
        return super().__str__() + f" - {self.schoolName}"
    

class ExternalAccess(models.Model):
    admin_name = models.CharField(max_length=255, null=True)
    admin_email = models.EmailField(unique=True, null=True)
    admin_password = models.CharField(max_length=255)

    def __str__(self):
        return super().__str__() + f" - {self.admin_email}"