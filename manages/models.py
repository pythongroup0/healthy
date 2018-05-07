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




class IngredientsInfo(models.Model):
    ingredientsName=models.CharField(max_length=40)
    water=models.FloatField(default=0.0)
    energy=models.IntegerField(default=0)
    protein=models.FloatField(default=0.0)
    fat=models.FloatField(default=0.0)
    saccharides=models.FloatField(default=0.0)
    price=models.FloatField(default=0.0)
    def setBatchAttr(self,ingredientsName,water,energy,protein,fat,saccharides,price):
        self.ingredientsName = ingredientsName
        self.water = water
        self.energy= energy
        self.protein = protein
        self.fat = fat
        self.saccharides = saccharides
        self.price = price

    def __str__(self):
        return 'ingredientsName:'+self.ingredientsName+",energy:"+\
               str(self.energy)+",price:"+str(self.price)

class DishInfo(models.Model):
    # 菜品名称
    dishName = models.CharField(max_length=30)
    # 菜品能量
    dishEnergy = models.FloatField()
    # 菜品价格
    dishPrice = models.FloatField()
    # 包含的食材
    ingredients = models.ManyToManyField(IngredientsInfo)
    # 分类
    type = models.CharField(max_length=20,default='')

    def setBatchAttr(self, dishName, dishEnergy, dishPrice):
        self.dishName = dishName
        self.dishEnergy = dishEnergy
        self.dishPrice = dishPrice

    def __str__(self):
        return 'dishName:' + self.dishName + ',dishEnergy:' + str(self.dishEnergy) + ',dishPrice:' + str(
            self.dishPrice)

class DishInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'dishName', 'dishEnergy', 'dishPrice','type']

class IngredientsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ingredientsName', 'water','energy','protein','fat'
                    ,'saccharides','price']