from django.contrib import admin
from .models import *


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Consulting)
class ConsultingAdmin(admin.ModelAdmin):
    pass
