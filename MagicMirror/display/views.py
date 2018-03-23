from django.shortcuts import render
from django.http import HttpResponse
from display.models import Devices, Tips, Weathers, News
import json, urllib.request

# Create your views here.

def index(request):
    return render(request, 'index.html')

def devices(request):
    devices_list = Devices.objects.all().order_by('location')
    return HttpResponse(json.dumps(devices_list),content_type='applicatiion/json')

def grab_weather(request):
    url='http://api.yytianqi.com/forecast7d?city=CH280101&key=f0mga9w4ths0bjgh'
    try:
        data_json = urllib.request.urlopen(url).read().decode('utf-8')
    except:
        print('Warning: Grap Weather Api FAILED!')
        return 1
    else:
        print('Congratulation: Grap Weather Api Succeed!')
        data_dict = json.loads(data_json)
        city_name = data_dict['data']['cityname']
        Weathers.objects.all().delete()                 #清空数据库旧数据
        try:                 
            for item in data_dict['data']['list']:          #逐天写入天气数据
                daily_weather = Weathers(city=city_name, date=item['date'], condition=item['tq1'], tempreture_low=item['qw2'], tempreture_high=item['qw1'])
                daily_weather.save()
        except:
            print('Warning: Write Weather Data FAILED!')
            return 1
        else:
            print('Congratulation: Write Weather Data Succeed!')
            Weathers.objects.order_by('date')       #按日期排序

    