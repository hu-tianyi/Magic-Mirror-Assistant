from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from display.models import Devices, Tips, Weathers, News
from django.core import serializers
import json, urllib.request

# Create your views here.

def index(request):
    return render(request, 'index.html')

def devices(request):
    devices_list = Devices.objects.all().order_by('location')
    return HttpResponse(json.dumps(devices_list),content_type='applicatiion/json')

def get_weather(request):
    url='http://api.yytianqi.com/forecast7d?city=CH280101&key=f0mga9w4ths0bjgh'
    try:
        data_json = urllib.request.urlopen(url).read().decode('utf-8')
    except:
        print('Warning: Grap Weather Api FAILED!')
        return 1
    else:
        print('Congratulation: Grap Weather Api Successfully!')
        data_dict = json.loads(data_json)
        #   print(data_dict)
        city_name = data_dict['data']['cityName']
        Weathers.objects.all().delete()                 #清空数据库旧数据
        try:                 
            for item in data_dict['data']['list']:          #逐天写入天气数据
                daily_weather = Weathers(city=city_name, date=item['date'], condition=item['tq1'], tempreture_low=item['qw2'], tempreture_high=item['qw1'])
                daily_weather.save()
        except:
            print('Warning: Write Weather Data FAILED!')
            return 1
        else:
            print('Congratulation: Write Weather Data Successfully!')
            Weathers.objects.order_by('date')       #按日期排序
            try:
                #weather_list = {}
                weather_list = Weathers.objects.all().order_by('date')       #从本地数据库获取天气数据
                #weather_list = Weathers._meta.get_all_field_names()
                #weather_list = Weathers.objects.values('city', 'date', 'condition', 'tempreture_low', 'tempreture_high').order_by('date')       #从本地数据库获取天气数据
            except:
                print('Warning: READ Weather Data FAILED!')
                return 1
            else:
                print('Congratulation: Read Weather Data Successfully!')
                try:
                    #weather_json = weather_list.toJSON()
                    weather_json = serializers.serialize('json', weather_list)
                    #weather_json = json.dumps(weather_list)
                    #print(isinstance(weather_json, str))
                    #weather_json = weather_json.strip('[', ']')
                    #print(weather_json)
                except:
                    print('Warning: Translate Weather Data FAILED!')
                    return 1
                else:
                    return render(weather_json, content_type = "application/json")



    


    