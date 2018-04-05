#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from display.models import Devices, Tips, Weathers, News
from django.core import serializers
from dwebsocket.decorators import accept_websocket,require_websocket
import json, urllib.request
import time
import datetime

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

def DecodedCharArrayFromByteStreamIn(stringStreamIn):
    #turn string values into opererable numeric byte values
    byteArray = [ord(character) for character in stringStreamIn]
    datalength = byteArray[1] & 127
    indexFirstMask = 2 
    if datalength == 126:
        indexFirstMask = 4
    elif datalength == 127:
        indexFirstMask = 10
    masks = [m for m in byteArray[indexFirstMask : indexFirstMask+4]]
    indexFirstDataByte = indexFirstMask + 4
    decodedChars = []
    i = indexFirstDataByte
    j = 0
    while i < len(byteArray):
        decodedChars.append( chr(byteArray[i] ^ masks[j % 4]) )
        i += 1
        j += 1
    return decodedChars

@accept_websocket
def frontend(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:    #如果是普通的http方法
            #message = request.GET['message']
            message = str.encode("http"+datetime.datetime.now)
            return HttpResponse(message)
        except:
            return render(request,'index.html')
    if request.is_websocket():
        #print("request is websocket")
        while True:
            try:
                data = Devices.objects.all().order_by('location')
            except:
                print('Warning: READ DEVICES Data FAILED!')
                return 1
            else:
                #print('Congratulation: Read DEVICES Data Successfully!')
                try:
                    data_json = serializers.serialize('json', data)
                    b_data_json = str.encode(data_json) #转成字节
                    request.websocket.send(b_data_json)
                except:
                    print('Warning: Websocket FAILED!')
            finally:
                time.sleep(1)

@accept_websocket
def websockettest(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            #message = str.encode("http"+datetime.datetime.now)
            return HttpResponse(message)
        except:
            return render(request,'index.html')
    else:
        for message in request.websocket:
            #message = str.encode("sdfasdfsafa")
            request.websocket.send(message)#发送消息到客户端

@accept_websocket
def sim_websocket(request):
    if request.is_websocket():
        for message in request.websocket:
            print(message)
            request.websocket.send(message)

@accept_websocket
def voice_socket(request):
    if request.is_websocket():
        for message in request.websocket:
            try:
                tip = Tips(tip=message.decode())
                tip.save()
            except:
                print("更新tips数据库失败")

@accept_websocket
def device_socket(request):
    if request.is_websocket():
        for message in request.websocket:
            message_str = str(message, encoding="utf-8")
            if message_str == "1emp":
                try:
                    device = Devices.objects.get(location=1)
                    device.status="无设备"
                    device.save()
                except:
                    print("更新排插数据失败！")
            if message_str == "1on":
                try:
                    device = Devices.objects.get(location=1)
                    device.status="开"
                    device.save()
                except:
                    print("更新排插数据失败！")
            if message_str == "1off":
                try:
                    device = Devices.objects.get(location=1)
                    device.status="关"
                    device.save()
                except:
                    print("更新排插数据失败！")
            if message_str == "2emp":
                try:
                    device = Devices.objects.get(location=2)
                    device.status="无设备"
                    device.save()
                except:
                    print("更新排插数据失败！")
            if message_str == "2on":
                try:
                    device = Devices.objects.get(location=2)
                    device.status="开"
                    device.save()
                except:
                    print("更新排插数据失败！")
            if message_str == "2off":
                try:
                    device = Devices.objects.get(location=2)
                    device.status="关"
                    device.save()
                except:
                    print("更新排插数据失败！")
            if message_str == "3emp":
                try:
                    device = Devices.objects.get(location=3)
                    device.status="无设备"
                    device.save()
                except:
                    print("更新排插数据失败！")
            if message_str == "3on":
                try:
                    device = Devices.objects.get(location=3)
                    device.status="开"
                    device.save()
                except:
                    print("更新排插数据失败！")
            if message_str == "3off":
                try:
                    device = Devices.objects.get(location=3)
                    device.status="关"
                    device.save()
                except:
                    print("更新排插数据失败！")

def testwebpage(request):
    return render(request,'websockettest.html')





    


    