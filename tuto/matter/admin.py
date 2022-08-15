from django.contrib import admin

from .models import Matter, Semester, Inscription


@admin.register(Matter)
class MatterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('number',)
    list_display_links = ('number',)


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'student',)
    list_display_links = ('pk', 'student',)
