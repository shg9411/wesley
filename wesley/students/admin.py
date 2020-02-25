from django.contrib import admin
from .models import Student, Teacher, Group, Study, StudyType, Problem, Absent


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


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    pass


@admin.register(StudyType)
class StudyTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    pass


@admin.register(Absent)
class AbsentAdmin(admin.ModelAdmin):
    pass
