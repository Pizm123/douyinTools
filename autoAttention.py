# -*- coding: utf-8 -*-
# 直播间自动点关注功能
import time
from my_common import adb_common

adb_common = adb_common.AdbCommon()

for i in range(200):
    # 点击观众
    adb_common.call('click', 'user_point')
    # 点击关注按钮
    adb_common.call('click', 'attention_point')
    # 点空白，针对已关注情况
    adb_common.call('click', 'blank_point')
    # 返回
    adb_common.call('go_back')
    # 滑动
    adb_common.call('slide', 'slide_point')
