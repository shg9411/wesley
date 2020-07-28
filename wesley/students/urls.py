from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .filters import StudentFilter, ConsultFilter
from django_filters.views import FilterView


app_name = 'students'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('students/<int:pk>/', views.StudentDV.as_view(), name='student-detail'),
    path('consults/<int:pk>/', views.ConsultDV.as_view(), name='consult-detail'),
    path('students/<int:pk>/delete/',
         views.StudentDelete.as_view(), name='student-delete'),
    path('consults/<int:pk>/delete/',
         views.ConsultDelete.as_view(), name='consult-delete'),
    path('consults/<int:pk>/edit/', views.ConsultUV.as_view(), name='consult-edit'),
    path('students/<int:pk>/edit/', views.StudentUV.as_view(), name='student-edit'),
    path('students/create/', views.StudentCV.as_view(), name='student-new'),
    path('consults/create/', views.ConsultCV.as_view(), name='consult-new'),
    path('consults/search/', FilterView.as_view(filterset_class=ConsultFilter,
                                                template_name='students/consult_filter.html'), name='consult-search'),
    path('students/search/', FilterView.as_view(filterset_class=StudentFilter,
                                                template_name='students/student_filter.html'), name='student-search'),
    path('students/', views.StudentLV.as_view(), name='student-list'),
    path('consults/', views.ConsultLV.as_view(), name='consult-list'),
]
