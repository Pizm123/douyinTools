class Test:
    def __init__(self):
        self.name = "pizm"

    def test(self, func):
        func()

    def click(self):
        print("click")

from my_common import adb_common

if __name__ == '__main__':
    # test = Test()
    # test.test(test.click)
    adb_common = adb_common.AdbCommon()

