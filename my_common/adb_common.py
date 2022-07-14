import os
import time

from my_common import config
from typing import List
import random


# adb管理类
class AdbCommon:
    def __init__(self):
        # 设备列表
        self.adb_devices: List[AdbDevice] = []
        self.get_devices()

    # 获取adb设备列表
    def get_devices(self):
        devices = os.popen("adb devices").readlines()
        for device in range(1, len(devices) - 1):
            serial_num = devices[device].replace("\tdevice\n", "")
            adb_device = AdbDevice(serial_num)
            self.adb_devices.append(adb_device)

    # 遍历执行设备方法
    def foreach_call(self, func_name, *params):
        for device in self.adb_devices:
            self.call(device, func_name, *params)
            time.sleep(0.3 + random.random() * 0.2)

    # 调用设备方法
    def call(self, device, func_name, *params):
        if func_name == "click":
            device.click(params[0])
        if func_name == "go_back":
            device.goback()
        if func_name == "slide":
            device.slide(params[0])
        if func_name == "update_input":
            device.update_input(params[0])
        if func_name == "two_click":
            device.two_click(params[0])
        if func_name == "send_adb_message":
            device.send_adb_message(params[0])
        if func_name == "screen":
            device.screen()


# 设备类
class AdbDevice:
    def __init__(self, serial_num):
        # 命令间隔时间
        self.sleepTime = 0.9 + random.random() * 0.2
        # 设备序列号
        self.serialNum = serial_num
        # 设备分辨率配置
        size = self.cmd("shell wm size").read()
        self.config = config.get_config(size)

    # 执行命令方法
    def cmd(self, command):
        command = "adb -s " + self.serialNum + " " + command
        res = os.popen(command)
        return res

    # 点击
    def click(self, point):
        command = "shell input tap " + self.config[point]['x'] + " " + self.config[point]['y']
        self.cmd(command)
        time.sleep(self.sleepTime)

    # 返回
    def goback(self):
        command = "shell input keyevent 4"
        self.cmd(command)
        time.sleep(self.sleepTime)

    # 滑动
    def slide(self, param):
        command = "shell input swipe " + self.config[param]['x1'] + " " + self.config[param]['y1'] + " " + \
                  self.config[param]['x2'] + " " + self.config[param]['y2'] + " " + self.config[param]['time']
        self.cmd(command)
        time.sleep(self.sleepTime)

    # 双击
    def two_click(self, point):
        for i in range(2):
            command = "shell input tap " + self.config[point]['x'] + " " + self.config[point]['y']
            self.cmd(command)
            time.sleep(0.1)
        time.sleep(self.sleepTime)

    # 发送adb消息
    def send_adb_message(self, msg):
        # 发送消息
        command = "shell am broadcast -a ADB_INPUT_TEXT --es msg '" + msg + "'"
        self.cmd(command)
        time.sleep(self.sleepTime + 1)

    # 切换输入法
    def update_input(self, in_put):
        self.cmd("shell ime set " + in_put)
        time.sleep(self.sleepTime)

    # 截取手机屏幕
    def screen(self):
        self.cmd("exec-out screencap -p > " + self.serialNum + "_temp.jpg")
        time.sleep(self.sleepTime)
