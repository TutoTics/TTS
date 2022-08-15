from django.contrib import admin
from .models import User, Student, Teacher


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')
    list_display_links = ('name', 'last_name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', )
    list_display_links = ('user', 'code',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'document',)
    list_display_links = ('user', 'document',)
