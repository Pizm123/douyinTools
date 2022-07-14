# -*- coding: utf-8 -*-
# 自动刷推荐视频 完播点赞评论
import time
import random
from my_common import config
from my_common import adb_common

# 配置文件
conf = config.get_config()

# 完播时间
playTime = 1
randomTime = 3

# 间隔时间
stopTime = 0.9


# 自动刷推荐视频
def auto_play_recommend():
    # 切换adb输入法
    adb_common.update_input("com.android.adbkeyboard/.AdbIME")
    for i in range(100):
        # 操作停留时间
        sleep_time_r = stopTime + random.random() * 0.2

        if check_video():
            # 完播
            time.sleep(playTime + random.random() * randomTime)
            # 点赞
            give_a_like(sleep_time_r)
            # # 关注
            # attention(sleep_time_r)
            # 评论
            comment(sleep_time_r)
        # 上滑
        adb_common.slide(conf['video_slide_point']['x1'], conf['video_slide_point']['y1'],
                         conf['video_slide_point']['x2'], conf['video_slide_point']['y2'],
                         conf['video_slide_point']['time'], sleep_time_r)

    # 切换adb输入法
    adb_common.update_input("com.sohu.inputmethod.sogou.xiaomi/.SogouIME")


# 检查视频是否可操作
def check_video():
    adb_common.screen()
    res = adb_common.ocr_fun()
    res = adb_common.video_image_ocr_result_analyse(res)
    return adb_common.is_conform_rules(res)


# 点赞功能
def give_a_like(sleep_time_r):
    adb_common.two_click(conf['user_point']['x'], conf['user_point']['y'], sleep_time_r)


# 主页关注功能
def attention(sleep_time_r):
    # 点击头像位置 进入主页
    adb_common.click(conf['head_point']['x'], conf['head_point']['y'], sleep_time_r)

    # 点击主页关注按钮（关注按钮位置浮动，多次点击）
    adb_common.click(conf['home_attention_point']['x'], conf['home_attention_point']['y'], sleep_time_r)
    adb_common.click(conf['home_attention_point']['x'], conf['home_attention_point']['y1'], sleep_time_r)

    # 点击主页空白位置
    adb_common.click(conf['home_blank_point']['x'], conf['home_blank_point']['y'], sleep_time_r)

    # 返回
    adb_common.goback(sleep_time_r)
    adb_common.goback(sleep_time_r)


# 评论功能
def comment(sleep_time_r):
    # 点击视频评论按钮
    adb_common.click(conf['comment_button_point']['x'], conf['comment_button_point']['y'], sleep_time_r)
    # 点击输入框位置
    adb_common.click(conf['input_point']['x'], conf['input_point']['y'], sleep_time_r)
    # 发送adb消息
    base_config = config.get_base_config()
    msgs = base_config['comment_msg']
    msg = msgs[random.randint(0, len(msgs) - 1)]
    adb_common.send_adb_message(msg)
    print(conf['send_button_point']['x'] + " " + conf['send_button_point']['y'])
    time.sleep(2)
    # 点击发送按钮
    adb_common.click(conf['send_button_point']['x'], conf['send_button_point']['y'], sleep_time_r)
    # 返回
    adb_common.goback(sleep_time_r)


if __name__ == '__main__':
    auto_play_recommend()
