from django.db import models

# Create your models here.
class Grades(models.Model):
    graObj = models.Manager()
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.gname
    
    class Meta:
        db_table='grades'
class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,self).get_queryset().filter(isDelete=False)
    def createStudent(self, name, age, gender, contend, grade,
         lastT, createT, isD=False):
         stu = self.model()
         stu.sanme = name
         stu.sage = age
         stu.sgender = gender
         stu.scontend = contend
         stu.sgrade = grade
         stu.lastTime = lastT
         stu.crateTime = createT
         return stu

         
         
class Students(models.Model):
    #自定义模型管理器
    stuObj = models.Manager()
    stuObj2 = StudentsManager()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE)
    lastTime = models.DateTimeField(auto_now=True)
    crateTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.sname

    class Meta:
        #定义数据表名，推荐使用小写字母
        db_table="students"
        #对象的默认排序字段，获取对象的列表时使用
        #注意排序会增加数据库的开销
        ordering=['id'] # 默认为升序，若为降序则加‘-’号，如[-'id']

        #定义一个类方法创建对象
    @classmethod
    def createStudent(cls, name, age, gender, contend, grade,
         lastT, createT, isD=False):
         stu = cls(sname = name, sage = age, sgender=gender, scontend = contend, sgrade=grade, lastTime=lastT, crateTime=createT, isDelete=isD)
         return stu