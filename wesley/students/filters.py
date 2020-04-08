from .models import Student, Consulting
import django_filters


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = '__all__'


class ConsultFilter(django_filters.FilterSet):
    class Meta:
        model = Consulting
        fields = '__all__'
