#-*-coding:utf-8-*- 
import paho.mqtt.client as mqtt
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

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # do something with msg
    print(msg.topic+" "+str(msg.payload))

#def on_publish(topic, payload, qos):
#    mqttClient.publish(topic, payload, qos)

client = mqtt.Client()
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