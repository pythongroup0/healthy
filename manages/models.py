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

class DishInfo(models.Model):
    #菜品名称
    dishName = models.CharField(max_length = 30)
    #菜品能量
    dishEnergy = models.FloatField()
    #菜品价格
    dishPrice = models.FloatField()
    #菜品分类
    dishClassify=models.CharField(default='meat',max_length=60)
    #包含食材
    dishIngredients=models.CharField(default='egg',max_length=120)

    def setBatchAttr(self,dishName,dishEnergy,dishPrice,dishClassify,dishIngredients):
        self.dishName = dishName
        self.dishEnergy = dishEnergy
        self.dishPrice = dishPrice
        self.dishClassify=dishClassify
        self.dishIngredients=dishIngredients

    def __str__(self):
        return 'dishName:'+self.dishName+',dishEnergy:'+str(self.dishEnergy)+',dishPrice:'+\
               str(self.dishPrice)+self.dishClassify+',dishIngredients:'+self.dishIngredients

class DishInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'dishName', 'dishEnergy', 'dishPrice','dishClassify','dishIngredients']


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

class IngredientsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ingredientsName', 'water','energy','protein','fat'
                    ,'saccharides','price']

class DishAndIngredient(models.Model):
    dishID=models.IntegerField()
    ingredientsID=models.IntegerField()
    ingredientsWeight=models.FloatField()

    def setBatchAttr(self,dishID,ingredientsID,ingredientsWeight):
        self.dishID=dishID
        self.ingredientsID=ingredientsID
        self.ingredientsWeight=ingredientsWeight

    def __str__(self):
        return 'dishId:'+str(self.dishID)+',IngredientsId:'+str(self.ingredientsID)+',ingredientsWeight:'+str(self.ingredientsWeight)

class DishIngredientsAdmin(admin.ModelAdmin):
    list_display = ['id','dishID','ingredientsID','ingredientsWeight']