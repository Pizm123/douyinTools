import os
import time
from paddleocr import PaddleOCR
from my_common import config

# 基础配置信息
base_config = config.get_base_config()


# 获取设备序列号
def get_adb_devices():
    devices = os.popen("adb devices")
    return devices


# 点击
def click(x, y, sleep_time):
    os.popen("adb shell input tap " + x + " " + y)
    time.sleep(sleep_time)


# 双击
def two_click(x, y, sleep_time):
    for i in range(2):
        os.popen("adb shell input tap " + x + " " + y)
        time.sleep(0.1)
    time.sleep(sleep_time)


# 返回
def goback(sleep_time):
    os.popen("adb shell input keyevent 4")
    time.sleep(sleep_time)


# 发送adb消息
def send_adb_message(msg):
    # 发送消息
    os.popen("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '" + msg + "'")


# 切换输入法
def update_input(in_put):
    os.popen("adb shell ime set " + in_put)
    time.sleep(0.5)


# 滑动
def slide(x1, y1, x2, y2, slide_time, sleep_time):
    os.popen("adb shell input swipe " + x1 + " " + y1 + " " + x2 + " " + y2 + " " + slide_time)
    time.sleep(sleep_time)


# 截取手机屏幕
def screen():
    os.popen("adb exec-out screencap -p > temp.jpg")
    time.sleep(0.5)


# 图片文字识别
def ocr_fun():
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    img_path = 'temp.jpg'
    result = ocr.ocr(img_path, cls=True)
    return result


# 首页推荐截图结果过滤
def video_image_ocr_result_analyse(result):
    if result is None:
        return None
    # 有效结果
    valid_res = []
    # 遍历结果数组
    for line in result:
        # 文字坐标
        point = line[0]
        # 文字坐标点
        left_top = point[0]
        right_bottom = point[2]

        # 顶部及底部文字丢弃
        if left_top[1] > 2220 or right_bottom[1] < 200:
            continue
        # 有效结果添加到结果数组
        valid_res.append(line)
    return valid_res


# 判断是否符合规则
def is_conform_rules(res):
    if res is None:
        return False
    is_conform = False
    for line in res:
        # 文字
        text = line[1][0]
        # 黑名单直接返回-不符合规则
        if is_exists_blacklist(text):
            print(False)
            return False
        # 存在白名单内，结果置为True
        if is_exists_white_list(text):
            is_conform = True
    print(is_conform)
    return is_conform


# 文字内容是否在白名单内
def is_exists_white_list(content):
    white_list = base_config['white_list']
    for s in white_list:
        if s.find(content) != -1 or content.find(s) != -1:
            return True
    return False


# 文字内容是否在黑名单内
def is_exists_blacklist(content):
    blacklist = base_config['blacklist']
    for s in blacklist:
        if s.find(content) != -1 or content.find(s) != -1:
            return True
    return False
