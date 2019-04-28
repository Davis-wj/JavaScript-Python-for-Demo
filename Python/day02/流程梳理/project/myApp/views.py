from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request,'myApp/index.html',)

from .models import Students,Grades
def students(request):
    studentsList = Students.stuObj2.all()
    return render(request,'myApp/students.html',{"students":studentsList})
def students2(request):
    #报异常，因为会查到多个值
    studentsList = Students.stuObj2.get(sgender=True)
    return HttpResponse("----------")
def students3(request):
    #只想显示前五条学生
    #注意在Django中下标不能时负数
    studentsList = Students.stuObj2.all()[0:5]
    return render(request, 'myApp/students.html', {"students": studentsList})
#分页显示学生
def stupage(request, num):
    page = int(num)
    studentsList = Students.stuObj2.all()[(num - 1) * 5:num * 5]
    return render(request, 'myApp/students.html', {"students": studentsList})
def studentSearch(request):
    # studentsList = Students.stuObj2.filter(sname__contains="王")
    # studentsList = Students.stuObj2.filter(pk__in=[2,4,6,8,10])
    # studentsList = Students.stuObj2.filter(sage__gte=30) #gt：大于 gte：大于等于 lt：小于 lte：小于等于
    # studentsList = Students.stuObj2.filter(Q(pk__lte=4) | Q(sage__gte=50))
    # studentsList = Students.stuObj2.filter(Q(pk__lte=4)) #只有一个Q对象时，就是一个匹配
    studentsList = Students.stuObj2.filter(~ Q(pk__lte=4)) #加~ 就是去反的意思
    return render(request, 'myApp/students.html', {"students": studentsList})

def addstudents(request):
    grade = Grades.graObj.get(pk=1)
    stu = Students.createStudent("王键", 25, True, "我叫王键", grade, "2017-8-10","2017-8-11")
    stu.save()
    return HttpResponse("Hello")
def addstudents2(request):
    grade = Grades.graObj.get(pk=1)
    stu = Students.stuObj2.createStudent("张学", 55, True, "我叫张学友", grade, "2017-8-10","2017-8-11")
    stu.save()
    return HttpResponse("Hello张需要")

from django.db.models import F,Q
def grades(request):
    # g = Grades.graObj.filter(ggirlnum__gt=F('gboynum'))
    # print(g)
    
    return HttpResponse("pppppp")