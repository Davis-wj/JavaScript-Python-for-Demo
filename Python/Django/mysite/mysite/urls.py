"""mysite URL Configuration

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
from django.urls import path,include,re_path
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),    
    path('grades/',views.grades, name='grades'),
    path('students/', views.students, name='students'),
    #path('<int:num>/', views.gradesStudents),
    re_path(r'^grades/(\d+)$', views.gradesStudents),
]#新版本直接用path就可以了，不需要在MyApp下面新建urls.py文件了!
# from django.conf.urls import include, url
# from django.contrib import admin
# urlpatterns = [
# url(r'^', include('myApp.urls')),
# url(r'^admin/', admin.site.urls),
# ]
