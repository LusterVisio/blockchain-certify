from django.db import models


# Create your models here.

class AdminLastIP(models.Model):
    admin_id = models.CharField(max_length=64, blank=True, null=True)
    last_ip_address = models.GenericIPAddressField(null=True, blank=True)
