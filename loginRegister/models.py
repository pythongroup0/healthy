from django.db import models
from django.contrib import admin

class UserInfo(models.Model):
    # 用户名
    username = models.CharField(max_length=30)
    # 密码
    password = models.CharField(max_length=40)
    #邮箱
    email=models.CharField(max_length=50)
    # 性别
    gender = models.BooleanField(default=True)
    # 身高
    height = models.FloatField(default=0)
    # 体重
    weight = models.FloatField(default=0)
    # 年龄
    age = models.IntegerField(default=0)
    # 过敏食物
    senstive = models.CharField(default='',max_length=225)
    # 偏好
    perfer = models.CharField(default='',max_length=225)

    def setBatchAttr(self,username,password,email,gender,height,weight,age,senstive,perfer):
        self.username = username
        self.password = password
        self.email=email
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.senstive = senstive
        self.perfer = perfer

    def __str__(self):
        return 'username:'+self.username+',password:'+self.password

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password','email','gender','height','weight'
                    ,'senstive','perfer']