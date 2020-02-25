from django import forms
from .models import Problem, Student

class ProblemCreateForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['student','problem']


class ProblemUpdateForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['student','problem','finished']


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'