from django.shortcuts import render,redirect,get_object_or_404
from accounts.models import *
from accounts.forms import *
from certificates_database.models import *

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from urllib import request
from django.db.models import Count, Sum, Q, F
from datetime import datetime
from datetime import timedelta
from datetime import datetime as dt

import datetime
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db import transaction
from .utils import send_email
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import auth
import requests
import json
from certificates_database.forms import CertificateForm


today = datetime.date.today()


@login_required
def admin_dashboard(request):
    if request.user.is_authenticated and request.user.is_staff:
        # Get the university associated with the logged-in admin
        university = UniversityProfile.objects.filter(user=request.user).first()

        if university:
            # Count users with is_school_admin and is_school_rep in this university
            admin_count = User.objects.filter(is_school_admin=True, profile__university=university).count()
            rep_count = User.objects.filter(is_school_rep=True, profile__university=university).count()
            
            # Count students, departments, and certificates in this university
            student_count = Student.objects.filter(university=university).count()
            department_count = Department.objects.filter(university=university).count()
            certificate_count = Certificate.objects.filter(student__university=university).count()
        else:
            admin_count = rep_count = student_count = department_count = certificate_count = 0

        context = {
            "admin_count": admin_count,
            "rep_count": rep_count,
            "student_count": student_count,
            "department_count": department_count,
            "certificate_count": certificate_count,
        }

        return render(request, "admin_user/dashboard.html", context)

    
@login_required
def admin_schools(request):
    if request.user.is_authenticated and request.user.is_staff:    
        universities = University.objects.all() 
        context = {
			'universities':universities,
		}   
    return render(request,'admin_user/schools.html',context)



@login_required
def admin_manage_users(request):
     subscribers = User.objects.filter(is_subscriber=True)
     context = {
          'subscribers':subscribers,
	 }
     return render(request, 'admin_user/manage_users.html',context)


@login_required
def admin_manage_schools(request):
    universities = University.objects.all() 
    
    context = {
        'universities':universities,
	 }
    return render(request, 'admin_user/manage_schools.html',context)


@login_required
def update_profile_security(request):
    user_id= request.user.pk
    user_profile_id = request.user.profile.pk

    user_info = get_object_or_404(User, id=user_id)

    profile_info = get_object_or_404(Profile, id= user_profile_id )

    form = SignUpForm(instance=user_info)
    profile_form = ProfileForm(instance=profile_info)
    context = {
         'form':form,
         'profile_form':profile_form,
    }
    return render(request, 'pages/security.html',context)


@login_required
def change_password(request):
    if request.method =="POST":

        new_password = request.POST.get("new_password")
        old_password = request.POST.get("old_password")
        confirm_password = request.POST.get("confirm_password")
        user = request.user

    if confirm_password != new_password:
        messages.error(request, 'password mismatch (new password and confirm password)')
        return redirect('account:update_profile_security')

    try:
        User.objects.filter(id=user.id).update(password=make_password(new_password))
        messages.success(request, 'password was successfully changed')
        return redirect('account:update_profile_security')
        
    except User.DoesNotExist:
        messages.error(request, ' An unforeseen error occured while attempting to change your password. Please retry')
        return redirect('account:update_profile_security')


@login_required
def user_update_profile(request,id):
    profile=Profile.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile,)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile updates successfully')
            return redirect('dashboard:update_profile_security')
    else:
        messages.error(request, 'something went wrong.unable to update profile ')
        return redirect('dashboard:update_profile_security')


@login_required
def user_update_basicinfo(request,id):
    profile= User.objects.get(id=id)

    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES, instance=profile,)
        if form.is_valid():
            form.save()

            messages.success(request, 'User info updated successfully')
            return redirect('dashboard:update_profile_security')
        else:
           messages.error(request, 'invalid form : something went wrong.unable to update user_info ')
           return redirect('dashboard:update_profile_security')
   
    else:
        messages.error(request, 'something went wrong.unable to update user_info ')
        return redirect('dashboard:update_profile_security')


 #list of admins and add new admin modal  
@login_required
def admins(request):
    admins = User.objects.filter(role="Admin")

    if request.method == 'POST':
        form = AddAdminForm(request.POST, request.FILES)
        if form.is_valid:
            admin = form.save(commit=False)
            admin.role = "Admin"
            admin.raw_password = "abcd123"
            admin.set_password("abcd123")
            admin.username = "admin" + str(random.randint(100,999))
            admin.save()

            form = AddAdminForm()
            context.update({
                'message': 'New admin added successfully',
                'form':form,
                'admins':admins

            })
        else:
            
            context.update({
                'error': form.errors, 
                'admins':admins               
            })

            form = AddAdminForm()
            context.update({
                'form':form,
            })

    else:
       
        form = AddAdminForm()
        context.update({
            'admins':admins,
            'form':form,
        })
    return render(request, "backend/users/admins.html", context)


# view single admin
@login_required
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.success(request, 'user deleted successfully')

    return redirect('dashboard:manage_users')
    

@login_required
def university_create(request):
    if request.method == "POST":
        form = UniversityProfileForm(request.POST, request.FILES)
        if form.is_valid():
            university = form.save(commit=False)
            university.user = request.user  # Assign the current user
            university.save()
            return redirect('dashboard:university_list')  # Redirect to the list view
    else:
        form = UniversityProfileForm()
    return render(request, 'admin_user/add_university.html', {'form': form})



@login_required
def university_list(request):
    university = UniversityProfile.objects.filter(user=request.user).first()
    return render(request, 'admin_user/profile.html', {'university': university})



@login_required
def university_update(request, pk):
    university = get_object_or_404(UniversityProfile, pk=pk)
    if request.method == "POST":
        form = UniversityProfileForm(request.POST, request.FILES, instance=university)
        if form.is_valid():
            form.save()
            return redirect('dashboard:university_list')
    else:
        form = UniversityProfileForm(instance=university)
    return render(request, 'admin_user/add_university.html', {'form': form})


@login_required
def university_delete(request, pk):
    university = get_object_or_404(UniversityProfile, pk=pk)
    if request.method == "POST":
        university.delete()
        return redirect('university_list')
    return render(request, 'university_confirm_delete.html', {'university': university})


@login_required
def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            university = UniversityProfile.objects.filter(user=request.user).first()
            if university:
                department.university = university
            department.save()
            messages.success(request,"University department Added Successfully")
            return redirect('dashboard:department_list')
    else:
        form = DepartmentForm()
    return render(request, 'admin_user/add_department.html', {'form': form})


@login_required
def department_list(request):
    # Get the university of the logged-in admin
    university = UniversityProfile.objects.filter(user=request.user).first()
    
    # Fetch departments belonging to this university
    departments = Department.objects.filter(university=university) if university else []

    return render(request, 'admin_user/manage_departments.html', {'departments': departments})


@login_required
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request,"Department update succesfully")
            return redirect('dashboard:department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'admin_user/add_department.html', {'form': form})


@login_required
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "GET":
        department.delete()
        messages.success(request, 'University  department successfully deleted')
        return redirect('dashboard:department_list')
    return redirect('dashboard:department_list')


@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
        
            student = form.save(commit=False)
            student.user = request.user
          
            university = UniversityProfile.objects.filter(user=request.user).first()
            if university:
                student.university = university
            student.save()
            messages.success(request,'Student was created successfully' )
            return redirect('dashboard:student_list')
    else:
        form = StudentForm()
    return render(request, 'admin_user/add_student.html', {'form': form})


@login_required
def student_list(request):
    # Get the university of the logged-in admin
    university = UniversityProfile.objects.filter(user=request.user).first()
    
    # Fetch students belonging to this university
    students = Student.objects.filter(university=university) if university else []

    return render(request, 'admin_user/manage_students.html', {'students': students})


@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "student Update succesfully")
            return redirect('dashboard:student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'admin_user/add_student.html', {'form': form})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "GET":
        student.delete()
        messages.success(request,'student delete successfully')
        return redirect('dashboard:student_list')
    return rediect('dashboard:student_list')



@login_required
def certificates(request):

    # Get the university of the logged-in user
    university = UniversityProfile.objects.filter(user=request.user).first()

    if university:
        # Get all certificates related to students in this university
        certificates = Certificate.objects.filter(student__university=university).select_related(
            "student", "student__department"
        )
    else:
        certificates = []

    return render( request,  "admin_user/students_certificates.html",  {"certificates": certificates})



@login_required
def create_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES, user=request.user)  # Pass the logged-in user
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user = request.user  # Assign the logged-in user
            certificate.save()
            messages.success(request, "Student's certificate was hashed with blockchain and added to the database successfully.")
            return redirect('dashboard:certificates')
        else:
            messages.error(request, "Something went wrong. The student's certificate was not processed.")
            return redirect('dashboard:certificates')
    else:
        form = CertificateForm(user=request.user)  # Pass the logged-in user
    return render(request, 'admin_user/hash_certificate.html', {'form': form})



@login_required
def update_certificate(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)  # Ensure the user owns the certificate
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES, instance=certificate)
        if form.is_valid():
            form.save()
            messages.success(request,"certificate updated successfully")
            return redirect('dashboard:certificates')
    else:
        form = CertificateForm(instance=certificate)
    return render(request, 'admin_user/hash_certificate.html', {'form': form})



@login_required
def delete_certificate(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)  # Ensure the user owns the certificate
    if request.method == 'GET':
        certificate.delete()
        messages.error(request, 'Cerificate deleted Successfully' )
        return redirect('dashboard:certificates')
    return redirect(request, 'dashboard:certificates')