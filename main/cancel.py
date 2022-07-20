import time

from my_common import adb_common, ocr_tools

if __name__ == '__main__':
    adb_common = adb_common.AdbCommon(0.3)
    devices = adb_common.adb_devices
    for device in devices:
        for i in range(200):
            adb_common.call(device, "screen")
            res = ocr_tools.ocr_fun("temp/" + device.serialNum + "_temp.jpg")
            points = ocr_tools.get_points_by_text(res, "互相关注")
            for point in points:
                x = str(point[0]).replace('.0', '')
                y = str(point[1]).replace('.0', '')
                adb_common.call(device, "click_point", x, y)
                adb_common.call(device, "click_point", "614", "1735")
            points2 = ocr_tools.get_points_by_text(res, "已关注")
            for point in points2:
                x = str(point[0]).replace('.0', '')
                y = str(point[1]).replace('.0', '')
                adb_common.call(device, "click_point", x, y)
            adb_common.call(device, "slide", "cancel_slide")
            time.sleep(2)
