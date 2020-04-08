from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class ConsultForm(forms.ModelForm):
    class Meta:
        model = Consulting
        fields = '__all__'


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
