local module = {}

module.SSID = {}
module.SSID["wifiname"] = "wifi password"

module.HOST = "mqtt broker host name"

module.PORT = mqtt broker port

module.USERNAME = "mqtt account user name"


module.PASSWORD = "mqtt account password"


--set relay pin
module.DEVICE = 1

module.ID = node.chipid()

module.ENDPOINT = "/nodemcu/"..node.chipid()

return module
