from my_common import adb_common
from my_common import ocr_tools

if __name__ == '__main__':
    adb_common = adb_common.AdbCommon(1)
    # adb_common.foreach_call('screen')
    res = ocr_tools.ocr_fun("temp/7c110d9e_temp.jpg")
    print(res)