from django.db import models
from django.contrib import admin

# Create your models here.
class AdminInfo(models.Model):
    #管理员账号
    adminname=models.CharField(max_length=30)
    #密码
    password=models.CharField(max_length=40)

class AdminInfoAdmin(admin.ModelAdmin):
    list_display = ['id','adminname','password']