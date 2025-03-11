from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom User Model
class User(AbstractUser):
    is_school_admin = models.BooleanField(default=True)
    is_school_rep = models.BooleanField(default=False)
 

# School Representative Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    university=models.ForeignKey("UniversityProfile", on_delete=models.CASCADE, blank=True, null = True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# University Profile Model
class UniversityProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="university_profile", blank=True, null= True)  # One admin can have only one university
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    motto = models.CharField(max_length=255, blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)
    university_type = models.CharField(max_length=50, choices=[('Public', 'Public'), ('Private', 'Private')], blank=True, null=True )
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to="university_logos/", blank=True, null=True)
    accreditation_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Department Model
class Department(models.Model):
    university = models.ForeignKey(UniversityProfile, on_delete=models.CASCADE, related_name="departments")
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    head_of_department = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.university.name}"


# Student Model
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    email = models.EmailField(unique=True, blank =True, null = True)
    fullname = models.CharField(max_length=100, blank=True, null =True)
    university = models.ForeignKey(UniversityProfile, on_delete=models.CASCADE, related_name="students", blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="students", blank=True, null=True)
    mat_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    course_of_study = models.CharField(max_length=255, blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    graduation_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.fullname} ({self.mat_number})"
