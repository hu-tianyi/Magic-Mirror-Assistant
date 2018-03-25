import json, urllib.request

url='http://api.yytianqi.com/forecast7d?city=CH280101&key=f0mga9w4ths0bjgh'
data_json = urllib.request.urlopen(url).read().decode('utf-8')
data_dict = json.loads(data_json)
for item in data_dict['data']['list']:
	print("日期："+item['date'])
	print("白天天气："+item['tq1'])
	print("白天气温："+item['qw1'])
