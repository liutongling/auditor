from django.db import models

# Create your models here.
from django.db import models


class Auditor(models.Model):
    auditorName = models.CharField(max_length=20)
    auditorUnit = models.CharField(max_length=50,default="null")
    Academypassword = models.IntegerField(default=0)
    AcademyNum = models.IntegerField(default=0)


class Academy(models.Model):
    Academyname = models.CharField(max_length=50)
    auditorName = models.ForeignKey(Auditor, on_delete=models.SET_NULL,null=True,) # 当审核人被删除之后学院设置为Null
    responsible1 = models.CharField(max_length=50,null=True)
    responsibleTel = models.CharField(max_length=50,null=True)
    NumPerson = models.IntegerField(default=0)