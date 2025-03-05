from django.urls import path
from . import views


app_name = "auth"


urlpatterns = [
   path('signup/', views.sign_up, name = "signup"),
   path('signin/', views.sign_in, name = "signin"),
   path('signout/', views.sign_out, name = "signout"),
   path('admin/add_user', views.add_admin_user, name = "adduser"),

]