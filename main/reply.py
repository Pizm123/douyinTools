# 评论区回复功能
import time

from my_common import adb_common
from my_common import ocr_tools
from concurrent.futures import ThreadPoolExecutor
from my_common import config
import random
from main import autoPlay

base_config = config.get_base_config()
msgs = base_config['reply_message']
# adb管理对象
adb_common = adb_common.AdbCommon(0.9)
# 线程池
pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix='测试线程')


# 访客类
class VisitorList:
    def __init__(self, device):
        self.device = device
        self.point = []

    # 获取回复按钮位置
    def get_reply_point(self):
        # 截图
        adb_common.call(self.device, 'screen')
        # 文字识别
        res = ocr_tools.ocr_fun("temp/" + self.device.serialNum + "_temp.jpg")
        # 获取回复按钮位置
        try:
            self.point = ocr_tools.get_point_by_text(res, "回复")
        except Exception as e:
            print(e)

    # 回复消息
    def reply_message(self):
        x = str(self.point[0]).replace('.0', '')
        y = str(self.point[1]).replace('.0', '')
        # 点击回复按钮
        # adb_common.call(self.device, "click_point", x, y)
        # # 输入回复信息
        # msg = msgs[random.randint(0, len(msgs) - 1)]
        # adb_common.call(self.device, 'send_adb_message', msg)
        # time.sleep(1)
        # # 点击发送按钮
        # adb_common.call(self.device, 'click', 'send_button_point')
        # 翻页
        adb_common.call(self.device, 'slide_by_point', "comments_next_page", x, y)

    # 回访评论区用户
    def follow_up(self):
        # 点击头像位置
        adb_common.call(self.device, 'click', 'comments_head_point')
        time.sleep(3)
        # 点击主页第一个视频
        adb_common.call(self.device, 'click', 'user_home_first_video')
        time.sleep(1)
        # 完播点赞评论
        video = autoPlay.Video(self.device)
        # 点赞
        video.give_a_like()
        # 评论
        video.comment()
        # 返回两次
        adb_common.call(self.device, 'go_back')
        adb_common.call(self.device, 'go_back')


# 评论区回复
def comments_reply(device):
    for i in range(200):
        # 访问者列表对象
        visitor = VisitorList(device)
        # 获取回复按钮位置
        visitor.get_reply_point()
        if not visitor.point:
            break
        visitor.follow_up()
        # 回复消息
        visitor.reply_message()
        time.sleep(1)


flag = {"isStop": False}


# 开始回复
def start():
    flag['isStop'] = False
    # 切换adb输入法
    adb_common.foreach_call('update_input', "com.android.adbkeyboard/.AdbIME")
    # 遍历设备
    for device in adb_common.adb_devices:
        pool.submit(comments_reply, device)


if __name__ == '__main__':
    start()
