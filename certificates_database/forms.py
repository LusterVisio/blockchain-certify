
from django import forms
from .models import Certificate
from accounts.models import Student

class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=70)




class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['student', 'nationality', 'achievement_date', 'certificate_score', 'serial_no', 'cert_front', 'cert_back']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'achievement_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'certificate_score': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 5}),
            'serial_no': forms.TextInput(attrs={'class': 'form-control'}),
            'cert_front': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'cert_back': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the logged-in user from kwargs
        super().__init__(*args, **kwargs)

        if user:
            # Filter students from the same university as the logged-in user
            university = user.university_profile  # Assuming the logged-in user has a university_profile
            students_without_certificates = Student.objects.filter(university=university).exclude(
                certificate__isnull=False
            )
            self.fields['student'].queryset = students_without_certificates
