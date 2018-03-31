# -*- coding: utf-8-*-
import sys
import os
import logging
#import 串口通信模块

reload(sys)
sys.setdefaultencoding('utf8')

WORDS = ["chazuo"]
SLUG = "chazuo"

def handle(text, mic, profile, wxbot=None):
    logger = logging.getLogger(__name__)
    try:
        if any(word in text for word in [u"开启", u"打开"]):
            if any(word in text for word in [u"一号", u"1号"])：
                #发送一号打开命令
                print('发送一号打开命令')
                mic.say('正在开启一号插座', cache=True)
            if any(word in text for word in [u"二号", u"2号"])：
                #发送二号打开命令
                print('发送二号打开命令')
                mic.say('正在开启二号插座', cache=True)
            if any(word in text for word in [u"三号", u"3号"])：
                #发送三号打开命令
                print('发送三号打开命令')
                mic.say('正在开启三号插座', cache=True)
        elif any(word in text for word in [u"关闭", u"关机"]):
            if any(word in text for word in [u"一号", u"1号"])：
                #发送一号关闭命令
                print('发送一号关闭命令')
                mic.say('正在关闭一号插座', cache=True)
            if any(word in text for word in [u"二号", u"2号"])：
                #发送二号关闭命令
                print('发送二号关闭命令')
                mic.say('正在关闭二号插座', cache=True)
            if any(word in text for word in [u"三号", u"3号"])：
                #发送三号关闭命令
                print('发送三号关闭命令')
                mic.say('正在关闭三号插座', cache=True)
    except Exception, e:
        logger.error(e)
        mic.say('抱歉，物联网控制插件出错', cache=True)

                                                            
def isValid(text):
    return any(word in text for word in [u"插座", u"物联网", u"排插"])
