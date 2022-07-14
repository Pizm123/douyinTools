# -*- coding: utf-8 -*-
# 直播间自动点关注功能
import os
import time
import random
from my_common import config
from my_common import adb_common

config = config.get_config()
stopTime = 0.9

for i in range(200):
    stopTimeR = stopTime + random.random() * 0.2

    # 点击观众
    os.popen("adb shell input tap " + config['user_point']['x'] + " " + config['user_point']['y'])
    # 暂停1s
    time.sleep(stopTimeR)
    # 点击关注按钮
    os.popen("adb shell input tap " + config['attention_point']['x'] + " " + config['attention_point']['y'])
    time.sleep(stopTimeR)
    # 点空白，针对已关注情况
    os.popen("adb shell input tap " + config['blank_point']['x'] + " " + config['blank_point']['y'])
    time.sleep(stopTimeR)
    # 返回
    os.popen("adb shell input keyevent 4")
    time.sleep(stopTimeR)
    # 滑动
    os.popen("adb shell input swipe " +
             config['slide_point']['x1'] + " " +
             config['slide_point']['y1'] + " " +
             config['slide_point']['x2'] + " " +
             config['slide_point']['y2'] + " " +
             config['slide_point']['time'] + " ")
    time.sleep(stopTimeR)
