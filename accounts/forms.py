from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import UniversityProfile, Department, Student



class SignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    password2 = forms.CharField(required = True)
   

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
          
            
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control', 'id':'name', 'placeholder':'First Name', 'id':'floatingInput', 'aria-describedby':'nameHelp'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control', 'id':'name', 'placeholder':'Last Name', 'id':'floatingInput','aria-describedby':'nameHelp'})
        self.fields['username'].widget.attrs.update({'class' : 'form-control', 'id':'name', 'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control', 'id':'email', 'placeholder':'Email'})
        self.fields['password'].widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form form-control px-5', 'id':'pass'})
        self.fields['password2'].widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'form form-control px-5', 'id':'re_pass'})
        

class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email or Username', 
                                                    'class':'form form-control px-5', 'name':'email', 'id':'your_name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 
                                                    'class':'form form-control px-5', 'id':'your_pass'}))



class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    #is_admin = forms.BooleanField(required=False)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name','username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'First Name'}),
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Last name'}),
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'}),
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'}),
        self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Passsword'}),
             


# University Form
class UniversityProfileForm(forms.ModelForm):
    class Meta:
        model = UniversityProfile
        fields = ['name', 'short_name', 'motto', 'established_date', 'university_type', 'address', 'phone_number', 'email', 'website', 'logo', 'accreditation_status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'motto': forms.TextInput(attrs={'class': 'form-control'}),
            'established_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'university_type': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control','rows': 2}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'accreditation_status': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }



# Department Form
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [ 'name', 'code', 'head_of_department', 'phone_number', 'email', 'established_date']
        widgets = {
           
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'head_of_department': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'established_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [ 'fullname', 'university', 'department', 'student_id', 'course_of_study', 'enrollment_date', 'graduation_date', 'phone_number', 'address', 'date_of_birth', 'is_active']
        widgets = {
  
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'course_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'graduation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control','rows': 2}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
