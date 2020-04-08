from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import *
from .forms import *
from .filters import StudentFilter
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'students/index.html')


class SchoolCV(LoginRequiredMixin, CreateView):
    login_url = '/login'
    template_name = 'students/school_new.html'
    success_url = '/schools'
    form_class = SchoolForm


class SchoolLV(ListView):
    model = School
    paginate_by = 20
    queryset = School.objects.all()


class ConsultCV(LoginRequiredMixin, CreateView):
    login_url = '/login'
    template_name = 'students/consult_new.html'
    success_url = '/consults'
    form_class = ConsultForm


class ConsultDV(DetailView):
    model = Consulting


class ConsultLV(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Consulting
    paginate_by = 20
    queryset = Consulting.objects.all()


class StudentLV(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Student
    paginate_by = 20
    #queryset = Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StudentLV, self).get_context_data(**kwargs)
        context['총원'] = Student.objects.all().count()
        context['배정'] = Student.objects.filter(status='재원' or '휴원').count()
        context['미배정'] = Student.objects.filter(type_choices='미배정').count()
        context['신규'] = Student.objects.filter(
            type_choices='신규').count()
        context['재입학'] = Student.objects.filter(
            type_choices='재입학').count()
        return context


class StudentCV(LoginRequiredMixin, CreateView):
    login_url = '/login'
    template_name = 'students/student_new.html'
    success_url = '/students'
    form_class = StudentForm


class ConsultUV(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Consulting
    context_object_name = 'consulting'
    form_class = ConsultForm
    template_name = 'students/consulting_edit.html'
    success_url = '/consults'

    def get_object(self):
        consult = get_object_or_404(Consulting, pk=self.kwargs['pk'])
        return consult


class StudentUV(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Student
    context_object_name = 'student'
    form_class = StudentForm
    template_name = 'students/student_edit.html'
    success_url = '/students'

    def get_object(self):
        student = get_object_or_404(Student, pk=self.kwargs['pk'])
        return student


class StudentDV(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDV, self).get_context_data(**kwargs)
        context['consult_list'] = Consulting.objects.filter(
            student=self.kwargs['pk'])
        return context


class StudentDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Student
    success_url = '/students'


class ConsultDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Consulting
    success_url = '/consults'
