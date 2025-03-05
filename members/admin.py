from django.contrib import admin
from .models import AdminLastIP


# Register your models here.

class AdminLastIpAdmin(admin.ModelAdmin):
    readonly_fields = ('admin_id', 'last_ip_address')
    list_display = ('admin_id', 'last_ip_address')


admin.site.register(AdminLastIP, AdminLastIpAdmin)
# primo da registrare è la classe modello
