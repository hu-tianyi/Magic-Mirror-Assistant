#coding=utf-8
from django.db import models

# Create your models here.

class Devices(models.Model):
    location = models.IntegerField(default = 1, null = False)
    status = models.IntegerField(default = 2, null = False)     # 0==关、1==开、2==空
    name = models.CharField(default = '请设置设备名<10字', max_length = 10, null = False)
    datetime = models.DateTimeField(auto_now_add = True)

class Tips(models.Model):
    tip = models.CharField(default = '请设置提示栏<20字', max_length = 20, null = False)
    def __str__(self):
        return self.tip


'''
class Weathers_predict(models.Model):
    city = 
    datetime = 
    tempreture = 
    humidity = 

class Weathers_now(models.Model):
    city = 
    datetime = 
    tempreture = 
    humidity = 

class News(models.Model):
    date = models.date()
    title = models.CharField(max_length = 40, null = False)
    content = models.CharField(max_length = 200, null = False)
'''