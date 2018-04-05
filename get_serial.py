# -*- coding: UTF-8 -*-
import serial
import time
from websocket import create_connection

ws = create_connection("ws://0.0.0.0:8000/sockets/")
while(True):
    try:
        ser = serial.Serial('/dev/ttyS0',115200)
        judge = ser.read()
        #一号设备
        if judge==b'0x10':
            ws.send("1emp")
        if judge==b'0x11':
            ws.send("1on")
        if judge==b'0x12':
            ws.send("1off")
        #二号设备
        if judge==b'0x20':
            ws.send("2emp")
        if judge==b'0x21':
            ws.send("2on")
        if judge==b'0x22':
            ws.send("2off")
        #三号设备
        if judge==b'0x20':
            ws.send("2emp")
        if judge==b'0x21':
            ws.send("2on")
        if judge==b'0x22':
            ws.send("2off")
    except:
        print("读取串口失败")
ws.close()

