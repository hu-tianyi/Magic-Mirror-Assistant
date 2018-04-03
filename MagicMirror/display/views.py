#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from display.models import Devices, Tips, Weathers, News
from django.core import serializers
from dwebsocket import require_websocket
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

def sockets(request):   #将排插数据写入数据库
    sockets_message = request.websocket.wait()  #获取客户端发来的指令
    if sockets_message=='设备一':  #对客户端指令进行分类
        try:
            Devices.objects.filter(location=1).delete()
        except:
            print('删除数据库-设备对象-旧数据 失败')
        else:
            print('删除数据库-设备对象-旧数据 成功')
        finally:
            try:
                if sockets_message=='关':
                    data = Devices(location=1, status=0, name='设备一')
                    data.save()
                if sockets_message=='开':
                    data = Devices(location=1, status=1, name='设备一')
                    data.save()
                if sockets_message=='空':
                    data = Devices(location=1, status=2, name='设备一')
                    data.save()
            except:
                print('数据库写入-设备对象 失败')
            else:
                print('数据库写入-设备对象 成功')
    # 复制 设备二
    # 复制 设备三
    return(1)


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

@require_websocket
def frontend(request):
    if request.is_websocket:
        #print("request is websocket")
        try:
            data = Devices.objects.all().order_by('location')
        except:
            print('Warning: READ DEVICES Data FAILED!')
            return 1
        else:
            print('Congratulation: Read DEVICES Data Successfully!')
            try:
                data_json = serializers.serialize('json', data)
                b_data_json = str.encode(data_json)
                #print(data_json)
                #request.websocket.send(data_json) #发送消息到客户端
                #print(DecodedCharArrayFromByteStreamIn(data_json))
                #request.websocket.send(DecodedCharArrayFromByteStreamIn(data_json))
                request.websocket.send(b_data_json)
            except:
                print('Warning: Websocket FAILED!')
    else:
        return render(request,'index.html')

@require_websocket
def websockettest(request):
    message = request.websocket.wait()
    #message = "sdadadsadsadas"
    print(message)
    request.websocket.send(message)

def testwebpage(request):
    return render(request,'websockettest.html')

def graphic(request):
    return(1)




    


    