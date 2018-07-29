# -*- coding: utf-8-*-
import picamera
#import numpy as np
import sys
import os
import face_rec
import logging
#import serial   #import 串口通信模块   迭代后弃用
import paho.mqtt.publish as publish #mqtt协议-publish

# mqtt 客户端配置
TOPIC = "/pi2mcu/"
HOST = "m13.cloudmqtt.com"
AUTH = {
    'username':"pi",
    'password':"pi"
}
PORT = 10045

reload(sys)
sys.setdefaultencoding('utf8')

WORDS = ["chazuo"]
SLUG = "chazuo"

def face_recog():
    name_0 = "Unknown"
    status = False
    #print("aaaaaaaaaaaaaaaaaaaaaa")
    try:
        name, status = face_rec.recognition(True)
    except Exception as e:
        print(e)
    print(name)
    print(status)
    if (status==True and name != name_0):
        return True
    else:
        return False
'''
def face_recog():
    return True
'''

def mqtt_publish(mic, message):
    try:
        publish.single(
            TOPIC,
            payload=message, 
            hostname = HOST, 
            auth = AUTH,
            # qos = 0,
            # tls=tls,
            port = PORT,
            #protocol=mqtt.MQTTv311
        )
    except:
        print("mqtt publish fail")
        mic.say('控制信息发送失败', cache=True)
    else:
        print("mqtt publish success")
        mic.say('控制信息发送成功', cache=True)

'''
def send_serial(mic, str_message):
    try:
        ser = serial.Serial("/dev/ttyAMA0",115200)
        #ser.open()
        b_message = str_message.encode('utf-8')
        ser.write(b_message)
        print("串口信息发送成功")
    except:
        mic.say('串口控制模块故障', cache=True)
'''

def face2mqtt(mic, str_message):
    mic.say('人脸识别授权中', cache=True)
    try:
        #result = face_recog()
        if (face_recog()):
            mic.say('识别成功,执行操作', cache=True)
            mqtt_publish(mic, str_message)
        else:
            mic.say('识别失败，重新识别中', cache=True)
            if (face_recog()):
                mic.say('识别成功', cache=True)
                mqtt_publish(mic, str_message)
            else:
                mic.say('识别失败，重新识别中', cache=True)
                if (face_recog()):
                    mic.say('识别成功', cache=True)
                    mqtt_publish(mic, str_message)
                else:
                    mic.say('三次识别失败，请重新再试', cache=True)
    except:
        mic.say('人脸识别模块故障', cache=True)

def handle(text, mic, profile, wxbot=None):
    logger = logging.getLogger(__name__)
    try:
        if any(word in text for word in [u"开启", u"打开"]):
            if any(word in text for word in [u"一号", u"1号"]):
                #发送一号打开命令
                print('发送一号打开命令')
                face2mqtt(mic, "nodemcu1on")
            if any(word in text for word in [u"二号", u"2号"]):
                #发送二号打开命令
                print('发送二号打开命令')
                face2mqtt(mic, "nodemcu2on")
            if any(word in text for word in [u"三号", u"3号"]):
                #发送三号打开命令
                print('发送三号打开命令')
                face2mqtt(mic, "nodemcu3on")
        elif any(word in text for word in [u"关闭", u"关机"]):
            if any(word in text for word in [u"一号", u"1号"]):
                #发送一号关闭命令
                print('发送一号关闭命令')
                face2mqtt(mic, "nodemcu1off")
            if any(word in text for word in [u"二号", u"2号"]):
                #发送二号关闭命令
                print('发送二号关闭命令')
                face2mqtt(mic, "nodemcu2off")
            if any(word in text for word in [u"三号", u"3号"]):
                #发送三号关闭命令
                print('发送三号关闭命令')
                face2mqtt(mic, "nodemcu3off")
    except Exception, e:
        logger.error(e)
        mic.say('抱歉，物联网控制插件出错', cache=True)

def isValid(text):
    return any(word in text for word in [u"插座", u"物联网", u"排插"])
