# -*- coding: utf-8 -*-
# 直播间自动点关注功能
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from my_common import adb_common

adb_common = adb_common.AdbCommon(0.4)

flag = {'isStop': False}


def auto_attention(params):
    for i in range(int(params['cycle_index'])):
        if flag['isStop']:
            break
        # 点击观众
        adb_common.foreach_call('click', 'user_point')
        # 点击关注按钮
        adb_common.foreach_call('click', 'attention_point')
        # 点空白，针对已关注情况
        adb_common.foreach_call('click', 'blank_point')
        # 返回
        adb_common.foreach_call('go_back')
        # 滑动
        adb_common.foreach_call('slide', 'slide_point')


# 开始关注
def start(*params):
    flag['isStop'] = False
    auto_attention(*params)


# 停止关注
def stop():
    flag['isStop'] = True
