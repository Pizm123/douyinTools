import time
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from my_common import adb_common, config
import random

adb_common = adb_common.AdbCommon(0.9)
base_config = config.get_base_config()
msgs = base_config['broadcast_room_msg']

if __name__ == '__main__':
    # 切换adb输入法
    adb_common.foreach_call('update_input', "com.android.adbkeyboard/.AdbIME")
    for i in range(500):
        # 点击输入框位置
        adb_common.foreach_call('click', 'broadcast_input_point')
        #
        for device in adb_common.adb_devices:
            # 发送adb消息
            msg = msgs[random.randint(0, len(msgs) - 1)]
            adb_common.call(device, 'send_adb_message', msg)
            # 点击发送按钮
            adb_common.call(device, 'click', 'broadcast_send_button_point')
        time.sleep(3)
