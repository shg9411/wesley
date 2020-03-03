from django.urls import path, include
from .views import ScheduleLV, StudentLV, StudentDV, index, ProblemLV, ProblemDV, ProblemCV, ProblemUV, delete_problem, StudentUV, StudentCV, delete_student


urlpatterns = [
    path('', index, name='index'),
    path('schedule/', ScheduleLV.as_view(), name='schedule'),
    path('student/', StudentLV.as_view(), name='student'),
    path('student/<int:pk>/', StudentDV.as_view(), name='student-detail'),
    path('student/<int:pk>/update/', StudentUV.as_view(), name='student-update'),
    path('problem/', ProblemLV.as_view(), name='problem'),
    path('problem/<int:pk>/', ProblemDV.as_view(), name='problem-detail'),
    path('problem/create/', ProblemCV.as_view(), name='problem-create'),
    path('problem/<int:pk>/update/', ProblemUV.as_view(), name='problem-update'),
    path('problem/<int:pk>/delete/', delete_problem, name='problem-delete'),
    path('student/<int:pk>/delete/', delete_student, name='student-delete'),
    path('student/create/', StudentCV.as_view(), name='student-create'),
]
