from django.db import models

class UserInfo(models.Model):
    # 用户名
    username = models.CharField(max_length=30)
    # 密码
    password = models.CharField(max_length=40)
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

    def __str__(self):
        return 'username:'+self.username+',password:'+self.password