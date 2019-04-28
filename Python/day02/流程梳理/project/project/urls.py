"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('students2/', views.students2, name='students2'),
    path('students3/', views.students3, name='students3'),    
    path('stu/<int:num>/', views.stupage),
    path('studentsearch/', views.studentSearch, name='studentSearch'),
    path('addstudents/', views.addstudents, name='addstudents'),
    path('addstudents2/', views.addstudents2, name='addstudents2'),
    path('grades/', views.grades),
]
