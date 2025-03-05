from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . forms import  SignUpForm, SignInForm, AddUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.mail import EmailMessage
from django.contrib import messages
from . utils import *
import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# sign in view
def sign_in(request):
    template ="pages/signin.html"
    if request.user.is_authenticated:
       return redirect('dashboard:admin_dashboard')

    if request.method == 'POST':

        form = SignInForm (request, data = request.POST) 
        if form.is_valid():
            cd = form.cleaned_data
            #next = request.GET.get('next') 
            #validate_next_url = url_has_allowed_host_and_scheme(next,allowed_hosts=None)
               
            user = authenticate(request,username=cd['username'], password=cd['password'])
                   
            if user is not None:
               

                if user is not None and user.is_authenticated and user.is_active: 
                    login(request,user)
                    username = user.username
                    return redirect('dashboard:admin_dashboard')
                        
                else:
                    messages.error(request, 'Incorrect Username or Pasword')
                    return redirect('auth:signin')
                               
        else:     
            messages.error(request, 'Incorrect Username or Pasword')
            return redirect('auth:signin')
                                 
    else:  
        form = SignInForm()            
        context = {
                'form':form
                }      
        return  render(request, template, context)

    
    
# sign up view
def sign_up(request):
    template = "pages/signup.html"

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            get_firstname = cd['first_name']
            get_lastname = cd['last_name']
            get_email = cd['email']
            get_username = cd['username']
            get_password1 = cd['password']
            get_password2 = cd['password2']

            User = get_user_model()  # Get the custom user model

            # Check if the username or email already exists
            if User.objects.filter(username=get_username).exists():
                messages.error(request, 'Error: Username already exists')
                return redirect('auth:signup')

            if User.objects.filter(email=get_email).exists():
                messages.error(request, 'Error: Email already exists')
                return redirect('auth:signup')

            if get_password1 != get_password2:
                messages.error(request, 'Passwords do not match')
                return redirect('auth:signup')

            # Create and save the new user
            user = User.objects.create_user(
                username=get_username,
                email=get_email,
                first_name=get_firstname,
                last_name=get_lastname,
                password=get_password1
            )
            user.save()

            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('auth:signin')

        else:
            messages.error(request, 'Invalid credentials, unable to create user.')
            return redirect('auth:signup')

    form = SignUpForm()
    context = {'form': form}
    return render(request, template, context)


# logout/signout view
def sign_out(request):
    logout(request)
    return redirect('home')
    
    
    
    
@login_required
def add_admin_user(request):
    template ="pages/add_admin_user.html"
    form = AddUserForm()

    if request.method =="POST":
        form = AddUserForm (request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            get_username = cd['username']
            form.save()
            messages.success(request, f'Admin user {get_username} was created successfully')
            return redirect('auth:add_admin')
        else:
            messages.error(request, 'Unable to create user try again')
            form = AddUserForm()
            context ={
                'form':form,
            }
            return render(request,template, context)
    context ={
        'form':form
    }
    return render(request, template, context)

