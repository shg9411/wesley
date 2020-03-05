from django import forms
from .models import Problem, Student, Temporary


class ProblemCreateForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['student', 'problem']


class ProblemUpdateForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['student', 'problem', 'finished']


class TemporaryUpdateForm(forms.ModelForm):
    class Meta:
        model = Temporary
        fields = ['student', 'temp_date', 'time']


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
