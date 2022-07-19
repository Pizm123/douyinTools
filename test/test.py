from my_common import adb_common
from my_common import ocr_tools
import os

if __name__ == '__main__':
    # 开启开发者模式
    # 开启USB安装
    # 开启USB调试(安全设置)
    res = os.popen("adb devices")
    # 安装adb输入法
    os.popen("adb install D:\project\python\douyinTools\\tools\ADBKeyboard.apk")
    #
    print(res.read())
