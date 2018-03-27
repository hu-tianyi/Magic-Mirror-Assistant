# -*- coding: utf-8-*-
import sys
import os
import logging

reload(sys)
sys.setdefaultencoding('utf8')

WORDS = ["chazuo"]
SLUG = "chazuo"

def handle(text, mic, profile, wxbot=None):
    logger = logging.getLogger(__name__)
    if SLUG not in profile or \
       'appId' not in profile[SLUG] or\
       'appSecret' not in profile[SLUG]:
        mic.say('插座配置有误，插件使用失败', cache=True)
        return
    appId = profile[SLUG]['appId']
    appSecret = profile[SLUG]['appSecret']
    sentence = getSentence(text)
    logger.info('sentence: ' + sentence)
    if sentence:
        try:
            s = translate(appId, appSecret, sentence)
            if s:
                mic.say(sentence+"的翻译是" + s, cache=False)
            else:
                mic.say("翻译" + sentence +"失败，请稍后再试", cache=False)
        except Exception, e:
            logger.error(e)
            mic.say('抱歉, 我不知道怎么翻译' + sentence, cache=False)
    else:
        mic.say(u"没有听清楚 请重试", cache=True)

                                                            
def isValid(text):
    return u"插座" in text
