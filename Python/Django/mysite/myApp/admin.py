from django.contrib import admin

# Register your models here.
from .models import Grades,Students
# Register
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    #列表页属性
    list_display = ['pk','gname','ggirlnum','gdate','gboynum',
     'isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 10

    #添加修改也属性
    # fields = ['gname','ggirlnum','gboynum','gdate','isDelete']
    fieldsets = [
        ('num',{"fields":['ggirlnum','gboynum']}),
        ('base',{'fields':['gname','gdate','isDelete']}),
    ]
admin.site.register(Grades, GradesAdmin)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别" #添加描述

    def delete(self):
        if self.isDelete:
            return "是"
        else:
            return "否"
    delete.short_description = "删除" #添加描述 只能描述函数

    list_display = ['pk','sname','sage',gender,'scontend','sgrade',delete]
    list_per_page = 10

    #执行动作位置更改
    actions_on_bottom = True
    actions_on_top = False
# admin.site.register(Students, StudentsAdmin) #以后使用装饰器进行注册