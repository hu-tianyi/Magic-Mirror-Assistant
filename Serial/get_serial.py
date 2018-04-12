# -*- coding: UTF-8 -*-
import serial
import time
from websocket import create_connection

ws = create_connection("ws://0.0.0.0:8000/sockets/")
while(True):
    try:
        time.sleep(0.1)
        ser = serial.Serial('/dev/ttyAMA0',115200)
        judge = ser.read(4)
        print(judge)
        #一号设备
        if judge==b'0x10':
            print("get 0x10")
            ws.send("1emp")
        if judge==b'0x11':
            print("get 0x11")
            ws.send("1on")
        if judge==b'0x12':
            print("get 0x12")
            ws.send("1off")
        #二号设备
        if judge==b'0x20':
            print("get 0x20")
            ws.send("2emp")
        if judge==b'0x21':
            print("get 0x21")
            ws.send("2on")
        if judge==b'0x22':
            print("get 0x22")
            ws.send("2off")
        #三号设备
        if judge==b'0x30':
            print("get 0x30")
            ws.send("3emp")
        if judge==b'0x31':
            print("get 0x31")
            ws.send("3on")
        if judge==b'0x32':
            print("get 0x32")
            ws.send("3off")
    except Exception as e:
        print(e)
ws.close()

