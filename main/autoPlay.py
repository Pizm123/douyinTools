# -*- coding: utf-8 -*-
# 自动刷推荐视频 完播点赞评论
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import time
import random
from my_common import config
from my_common import adb_common
from my_common import ocr_tools
from concurrent.futures import ThreadPoolExecutor

# 完播时间
playTime = 1
randomTime = 3

# adb管理对象
adb_common = adb_common.AdbCommon(0.9)
# 线程池
pool = ThreadPoolExecutor(max_workers=5, thread_name_prefix='测试线程')


# 短视频对象
class Video:
    def __init__(self, device):
        self.device = device

    # 检查视频是否可操作
    def check_video(self, black_list, white_list):
        adb_common.call(self.device, 'screen')
        res = ocr_tools.ocr_fun("temp/" + self.device.serialNum + "_temp.jpg")
        res = ocr_tools.video_image_ocr_result_analyse(res)
        if black_list is not None:
            ocr_tools.set_black_list(black_list)
        if white_list is not None:
            ocr_tools.set_white_list(white_list)
        return ocr_tools.is_conform_rules(res)

    # 完播
    def play_over(self, play_time):
        time.sleep(play_time + random.random() * randomTime)

    # 点赞功能
    def give_a_like(self):
        adb_common.call(self.device, 'two_click', 'user_point')

    # 评论功能
    def comment(self):
        # 点击视频评论按钮
        adb_common.call(self.device, 'click', 'comment_button_point')
        # 点击输入框位置
        adb_common.call(self.device, 'click', 'input_point')
        # 发送adb消息
        base_config = config.get_base_config()
        msgs = base_config['comment_msg']
        msg = msgs[random.randint(0, len(msgs) - 1)]
        adb_common.call(self.device, 'send_adb_message', msg)
        # 点击发送按钮
        adb_common.call(self.device, 'click', 'send_button_point')
        # 返回
        adb_common.call(self.device, 'go_back')

    # 下一个视频
    def next_video(self):
        adb_common.call(self.device, 'slide', "video_slide_point")


flag = {"isStop": False}


# 生成视频对象
def build_video(device, params):
    print(params)
    try:
        for i in range(int(params['cycle_index'])):
            if flag['isStop']:
                print("停止任务")
                break
            video = Video(device)
            if params['is_use_ocr'] == 2 or \
                    (params['is_use_ocr'] == 1 and video.check_video(params['black_list'], params['white_list'])):
                # 完播
                video.play_over(float(params['a_play_time']))
                # 点赞
                video.give_a_like()
                # 评论
                video.comment()
            video.next_video()
        print("刷推荐结束")
    except Exception as e:
        print(e,'error')


# 刷视频开始
def start(*params):
    print(params)
    flag['isStop'] = False
    # 切换adb输入法
    adb_common.foreach_call('update_input', "com.android.adbkeyboard/.AdbIME")
    # 遍历设备
    for device in adb_common.adb_devices:
        pool.submit(build_video, device, *params)

    # 切换普通输入法
    # adb_common.foreach_call('update_input', "com.sohu.inputmethod.sogou.xiaomi/.SogouIME")


# 停止刷视频
def stop():
    flag['isStop'] = True


if __name__ == '__main__':
    start()
