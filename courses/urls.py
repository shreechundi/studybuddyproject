from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profileview, name='profile'),
    path('<int:pk>/', views.Courseview, name='course_pk'),
    path('students/<pk>/', views.Profileview, name='profile_pk'),
    path('depts/', views.Departmentview, name='Departmentview'),
    path('deptclasses/', views.classview, name='classlist'),
    path('profileedit/', views.ProfileEdit, name='profileedit'),
]