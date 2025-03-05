from django.contrib import admin

# Register your models here.
from . models import User, UniversityProfile, Profile, Department, Student

admin.site.register(User)
admin.site.register(UniversityProfile)
admin.site.register(Profile)
admin.site.register(Department)
admin.site.register(Student)

