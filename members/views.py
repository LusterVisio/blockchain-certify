from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from ipware import get_client_ip
from .models import AdminLastIP


# Create your views here.


# def login_superuser(request):
#     ip, is_routable = get_client_ip(request)
#     if ip is None:
#         ip = "0.0.0.0"
#     last_ip = ip
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if request.user.is_authenticated:
#             return render(request, 'registration/login.html')
#         if user is not None and user.is_superuser:

#             try:
#                 obj = AdminLastIP.objects.get(admin_id=username)
#                 if obj.last_ip_address == last_ip:
#                     pass
#                 else:
#                     messages.success(request,
#                                      "Warning! This Admin User IP address is different from the last one used!")
#                     obj.last_ip_address = last_ip
#                     obj.save()

#             except AdminLastIP.DoesNotExist:
#                 new_admin_register = AdminLastIP(admin_id=username, last_ip_address=last_ip)
#                 new_admin_register.save()

#             login(request, user)
#             return redirect('/admin')

#         else:
#             # Return an 'invalid login' error message.
#             messages.success(request,
#                              "There was an error logging in, either you are not an admin user or credentials are wrong. Try again!")
#             return redirect('login')

#     else:
#         return render(request, 'registration/login.html', {})
