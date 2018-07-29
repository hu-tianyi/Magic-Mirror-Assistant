#-*-coding:utf-8-*-
import paho.mqtt.client as mqtt
from websocket import create_connection
import time

HOST = "m13.cloudmqtt.com"
PORT = 10045
USER = "pi"
PW = "pi"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # rc is the connection result
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/mcu2pi/")

'''
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)
'''

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    try:
        ws = create_connection("ws://0.0.0.0:8000/sockets/")
    except:
        print("get_mqtt.py: Create Websocket Connection failed")
    else:
        # do something with msg
        print("Mqtt Client: "+msg.topic+" "+str(msg.payload))
        judge = str(msg.payload)
        print(judge)
        #一号设备
        if judge==b'nodemcu1emp':
            ws.send("1emp")
        if judge==b'nodemcu1on':
            ws.send("1on")
        if judge==b'nodemcu1off':
            ws.send("1off")
        #二号设备
        if judge==b'nodemcu2emp':
            ws.send("2emp")
        if judge==b'nodemcu2on':
            ws.send("2on")
        if judge==b'nodemcu2off':
            ws.send("2off")
        #三号设备
        if judge==b'nodemcu3emp':
            ws.send("3emp")
        if judge==b'nodemcu3on':
            ws.send("3on")
        if judge==b'nodemcu3off':
            ws.send("3off")
    finally:
        ws.close()
    
try:
    time.sleep(5)
    client = mqtt.Client()
    #set client Username and Password
    client.username_pw_set(USER, PW)
    client.on_connect = on_connect
    client.on_message = on_message

    # Heartbeat period 120s
    client.connect(HOST, PORT, 120)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
except:
    print("get_mqtt.py: Mqtt Client failed")
else:
    print("get_mqtt.py: Working Properly")