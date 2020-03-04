from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Student, Problem, Regular, Temporary, Teacher
from .forms import ProblemCreateForm, ProblemUpdateForm, StudentUpdateForm
#from django.core.paginator import Paginator
import datetime


class ProblemLV(ListView):
    template_name = 'students/problem_list.html'
    context_object_name = 'problem_list'

    def get_queryset(self):
        return Problem.objects.filter(finished=False)


class ScheduleLV(ListView):
    template_name = 'students/study_list.html'
    context_object_name = 'temp_list'
    
    def get_queryset(self):
        return datetime.datetime.now()
    


class StudentLV(ListView):
    template_name = 'students/student_list.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.all()


class StudentDV(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'


class ProblemDV(DetailView):
    model = Problem
    template_name = 'students/problem_detail.html'
    context_object_name = 'problem'


class TemporaryDV(DetailView):
    model = Temporary
    template_name = 'students/temp_detail.html'
    context_object_name = 'temp'


def index(request):
    return render(request, 'students/index.html')


class ProblemCV(CreateView):
    model = Problem
    fields = ('student', 'problem')


class ProblemUV(UpdateView):
    context_object_name = 'problem'
    form_class = ProblemUpdateForm
    template_name = 'students/problem_update.html'

    def get_object(self):
        problem = get_object_or_404(Problem, pk=self.kwargs['pk'])
        return problem


class StudentCV(CreateView):
    model = Student
    fields = '__all__'


class StudentUV(UpdateView):
    context_object_name = 'student'
    form_class = StudentUpdateForm
    template_name = 'students/student_update.html'

    def get_object(self):
        student = get_object_or_404(Student, pk=self.kwargs['pk'])
        return student


def delete_problem(request, pk):
    Problem.objects.get(pk=pk).delete()
    return redirect('problem')


def delete_student(request, pk):
    Student.objects.get(pk=pk).delete()
    return redirect('student')
