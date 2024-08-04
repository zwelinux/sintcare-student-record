from django.contrib import admin

# Register your models here.

from .models import User, Course, Registration, Instructor

admin.site.register(User)

admin.site.register(Course)

admin.site.register(Registration)

admin.site.register(Instructor)
