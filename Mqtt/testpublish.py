import paho.mqtt.publish as publish
TOPIC = "/pi2mcu/"
HOST = "m13.cloudmqtt.com"
AUTH = {
    'username':"pi",
    'password':"pi"
}
PORT = 10045

publish.single(
    TOPIC,
    payload="this is message", 
    hostname = HOST, 
    auth = AUTH,
    # qos = 0,
    # tls=tls,
    port = PORT,
    #protocol=mqtt.MQTTv311
)