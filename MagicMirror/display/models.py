#coding=utf-8
from django.db import models
import json

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

class Weathers(models.Model):
    city = models.CharField(default = '城市名<10字', max_length = 10, null = False)
    date = models.DateField(null = False)
    condition = models.CharField(default = '天气状况<10字', max_length = 10, null = False)
    tempreture_low = models.IntegerField(default = 0, null = False)
    tempreture_high = models.IntegerField(default = 100, null = False)

    def toJSON(self):
        import json    
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class News(models.Model):
    date = models.DateField(null = False)
    title = models.CharField(max_length = 40, null = False)
    content = models.CharField(max_length = 200, null = False)