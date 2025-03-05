from django.contrib import admin
from django.forms.models import model_to_dict
import json
import hashlib
from django.core.serializers.json import DjangoJSONEncoder
from .models import Certificate
from .utils import sendTransaction  # Ensure you have a utility function to send transactions


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'nationality', 'certificate_score', 'achievement_date')
    list_filter = ('certificate_score',)
    search_fields = ("student__fullname__startswith",)
    readonly_fields = ('hash', 'txId')

    def save_model(self, request, obj, form, change):
        dict_for_json = model_to_dict(obj, fields={
            'student', 'nationality', 'achievement_date', 'certificate_score', 'issuance_date'
        })
        json_for_hash = json.dumps(dict_for_json, sort_keys=True, indent=4, cls=DjangoJSONEncoder)

        obj.hash = hashlib.sha256(json_for_hash.encode('utf-8')).hexdigest()
        obj.txId = sendTransaction(obj.hash)

        super().save_model(request, obj, form, change)


admin.site.register(Certificate, CertificateAdmin)
