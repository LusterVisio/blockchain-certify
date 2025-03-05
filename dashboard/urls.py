from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
   
   path('admin/', views.admin_dashboard, name="admin_dashboard"),
   path('admin/schools/', views.admin_schools, name="admin_school"),
   path('admin/students/', views.student_list, name='student_list'),
   path('admin/departments/', views.department_list, name='department_list'),
   path('admin/manage_users/', views.admin_manage_users, name="manage_users"),
   path('admin/manage_schools/', views.admin_manage_schools, name="manage_schools"),
   path('admin/students/certificate/', views.certificates, name="certificates"),
   path('admin/student/certificates/create/', views.create_certificate, name='create_certificate'),
    path('admin/student/certificates/update/<int:pk>/', views.update_certificate, name='update_certificate'),
    path('admin/student/certificates/delete/<int:pk>/', views.delete_certificate, name='delete_certificate'),


   path('admin/university/', views.university_list, name="university_list"),
   path('admin/university/add/', views.university_create, name="university_create"),
   path('admin/university/<int:pk>/edit', views.university_update, name="university_update"),
   path('admin/university/department/add/', views.department_create, name="department_create"),
   path('admin/university/department/<int:pk>/edit', views.department_update, name="department_update"),
   path('admin/university/department/<int:pk>/delete', views.department_delete, name="department_delete"),

   path('admin/university/department/student/', views.student_create, name="student_create"),
   path('admin/university/department/student/<int:pk>/edit', views.student_update, name="student_update"),
   path('admin/university/department/student/<int:pk>/delete', views.student_delete, name="student_delete"),


   path('admin/delete_user/<int:pk>/', views.delete_user, name="delete_user"),  
   path('update_profile_security/', views.update_profile_security, name="update_profile_security"),
   path('update_password/', views.change_password, name="change_password"),
   path('update_profile/<int:id>/', views.user_update_profile, name="user_update_profile"),
   path('update_basicinfo/<int:id>/', views.user_update_basicinfo, name="user_update_basicinfo"),
    

]
