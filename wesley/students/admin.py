from django.contrib import admin
from .models import Student, Teacher, Group, Regular, Temporary, Problem


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_number',)
    ordering = ('room_number',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Regular)
class RegularAdmin(admin.ModelAdmin):
    pass

@admin.register(Temporary)
class TemporaryAdmin(admin.ModelAdmin):
    pass

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    pass