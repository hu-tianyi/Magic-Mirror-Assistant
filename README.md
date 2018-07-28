# 魔镜精灵助手 Magic Mirror  Assistant

## 项目历程 Project Record

2018-03-20
本作品作为广州市电子设计十校联赛项目设立
2018-07-20
本作品已升级为广东省大学生电子设计大赛项目

## 交互模块 Interact module

### 硬件 Hardware

1. 树莓派3B Raspberry Pi 3B
2. 单向透视玻璃 Half Mirror
3. 显示器 Monitor
4. 麦克风 Microphone
5. 摄像头 Camera
6. 扬声器 Speaker

### 软件 Software 

#### 开发语言 Develop Language

1. Python 2.7 & 3.5
2. HTML + CSS +Javascript
3.  websocket

#### 关键技术 Key Technique

1. Django 1.11.11
2. Websocket

## 控制模块 Control module

### 硬件 Hardware

1. 物联网模块 Nodemcu
2. 变压器 220v → 5v
3. 继电器 Relay

### 软件 Software 

#### 开发语言 Develop Language

Lua

#### 关键技术 Key Technique

1. 通信协议 MQTT
2. 传输协议 I2C



## 开发环境 Environment

```
sudo pip3 install django==1.11.11
sudo pip install websocket-client
sudo pip3 install dwebsocket
sudo apt-get install python3-serial
sudo apt-get install python3-yaml
```

------

## 计划开发 Todo



## 正在开发 Doing



## 已经实现 Done

- 构思数据库结构 20th, Mar
- 搭建后台 21th, Mar
- 搭建前端时间模块 21th, Mar
- 天气api接口调用 23th, Mar
- 搭建前端天气模块 24th, Mar
- 交互界面大致布局 25th, Mar
- 语音交互系统 27th, Mar
- 搭建前端设备状态模块 28th, Mar
- 协调与单片机的通信协议 3rd, April
- 前后端websocket通信 4th, April
- python 模拟websocket通信 
- 调用api接口
- 部署开发服务器
- 与单片机联调
- 前端UI美化

