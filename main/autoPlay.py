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
adb_common = adb_common.AdbCommon()
# 线程池
pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix='测试线程')


# 短视频对象
class Video:
    def __init__(self, device):
        self.device = device

    # 检查视频是否可操作
    def check_video(self):
        adb_common.call(self.device, 'screen')
        res = ocr_tools.ocr_fun("temp/" + self.device.serialNum + "_temp.jpg")
        res = ocr_tools.video_image_ocr_result_analyse(res)
        return ocr_tools.is_conform_rules(res)

    # 完播
    def play_over(self):
        time.sleep(playTime + random.random() * randomTime)

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
def build_video(device):
    for i in range(200):
        if flag['isStop']:
            print("停止任务")
            break
        video = Video(device)
        if video.check_video():
            # 完播
            # video.play_over()
            # 点赞
            video.give_a_like()
            # 评论
            video.comment()
        video.next_video()


# 刷视频开始
def start():
    flag['isStop'] = False
    # 切换adb输入法
    adb_common.foreach_call('update_input', "com.android.adbkeyboard/.AdbIME")
    # 遍历设备
    for device in adb_common.adb_devices:
        pool.submit(build_video, device)

    # 切换普通输入法
    # adb_common.foreach_call('update_input', "com.sohu.inputmethod.sogou.xiaomi/.SogouIME")


# 停止刷视频
def stop():
    flag['isStop'] = True


if __name__ == '__main__':
    start()

# # 主页关注功能
# def attention(sleep_time_r):
#     # 点击头像位置 进入主页
#     adb_common.click(conf['head_point']['x'], conf['head_point']['y'], sleep_time_r)
#
#     # 点击主页关注按钮（关注按钮位置浮动，多次点击）
#     adb_common.click(conf['home_attention_point']['x'], conf['home_attention_point']['y'], sleep_time_r)
#     adb_common.click(conf['home_attention_point']['x'], conf['home_attention_point']['y1'], sleep_time_r)
#
#     # 点击主页空白位置
#     adb_common.click(conf['home_blank_point']['x'], conf['home_blank_point']['y'], sleep_time_r)
#
#     # 返回
#     adb_common.goback(sleep_time_r)
#     adb_common.goback(sleep_time_r)
