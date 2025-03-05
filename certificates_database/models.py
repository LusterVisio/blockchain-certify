from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from  accounts.models import Student
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name="certificate", null=True, blank=True )
    nationality = models.CharField(max_length=255, null=True)
    achievement_date = models.DateField()
    certificate_score = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(0)])
    issuance_date = models.DateTimeField(default=timezone.now)
    serial_no = models.CharField(max_length=20, unique=True ,blank=True, null=True)
    cert_front = models.ImageField(upload_to="certificates/", blank=True, null=True)
    cert_back = models.ImageField(upload_to="certificates/", blank=True, null=True)
    hash = models.CharField(max_length=66, default=None, null=True, blank=True)
    txId = models.CharField(max_length=66, default=None, null=True, blank=True)

    def __str__(self):
        return self.student.fullname

class AdminIP(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
