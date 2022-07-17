# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
from functools import partial
from main import autoPlay


# 初始化主窗体
def frame_init(window):
    # 设置标题
    root.title("自动营销工具")
    # 设置窗口大小变量
    width = 400
    height = 400
    # 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(size_geo)


# 主页类
class Index(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置菜单
        self.menu_init(parent)
        self.pack(expand=1, fill="both")
        lab = tk.Label(self, text="欢迎使用斗音自动工具\n请点击功能菜单或下方按钮开始使用", font=('宋体', 14))
        lab.grid(row=0, padx=50, pady=15)
        for (i, text) in ([(1, "刷推荐"), (2, "直播间关注"), (3, "直播间刷屏")]):
            but = tk.Button(self, text=text, command=partial(self.change, text), width=30)
            but.grid(row=i, padx=50, pady=15)
        # 根据鼠标左键单击事件，切换页面

    # 设置菜单
    def menu_init(self, window):
        # 创建一个主目录菜单，也被称为顶级菜单
        main_menu = Menu(window)
        for menu_map in [{"功能": ["刷推荐", "直播间关注", "直播间刷屏"]}, {"配置": []}, {"帮助": []}]:
            menu = Menu(main_menu, tearoff=False)
            for key in menu_map.keys():
                for i in menu_map.get(key):
                    menu.add_command(label=i, command=partial(self.change, i))
                main_menu.add_cascade(label=key, menu=menu)
        # 显示菜单
        window.config(menu=main_menu)

    def change(self, name):
        res = name
        for i in self.winfo_children():
            i.destroy()
        if res == "刷推荐":
            AutoPlay(self)
        elif res == "直播间关注":
            Page2(self)
        elif res == "直播间刷屏":
            Page3(self)


# 刷推荐视频页面
class AutoPlay(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 循环次数
        self.cycle_index = tk.StringVar()
        # 单视频播放时间
        self.a_play_time = tk.StringVar()
        # 是否过滤关键词
        self.is_use_ocr = tk.IntVar()

        self.pack(expand=1, fill="both")
        lab = tk.Label(self, text="自动刷推荐视频,完播点赞评论功能", font=('宋体', 14))
        lab.place(x=50, y=20, height=30)
        # 循环播放次数
        tk.Label(self, text="循环播放次数：").place(x=50, y=60, height=30)
        tk.Entry(self, textvariable=self.cycle_index).place(x=180, y=60, height=30)
        tk.Label(self, text="次").place(x=330, y=60, height=30)

        tk.Label(self, text="单视频播放时间：").place(x=50, y=100, height=30)
        tk.Entry(self, textvariable=self.a_play_time).place(x=180, y=100, height=30)
        tk.Label(self, text="秒").place(x=330, y=100, height=30)

        # 是否使用视频过滤功能
        tk.Label(self, text="是否过滤关键词").place(x=50, y=140)
        # 根据单选按钮的 value 值来选择相应的选项
        self.is_use_ocr.set(2)
        # 使用 variable 参数来关联 IntVar() 的变量 v
        tk.Radiobutton(self, text="是", indicatoron=False, variable=self.is_use_ocr, value=1).place(x=180, y=140)
        tk.Radiobutton(self, text="否", indicatoron=False, variable=self.is_use_ocr, value=2).place(x=230, y=140)

        # 关键词黑名单
        tk.Label(self, text="关键词黑名单：").place(x=50, y=180, height=30)
        self.black_list = Text(self, width=20, height=60, undo=True, autoseparators=False)
        self.black_list.place(x=180, y=180, height=60)
        # 关键词白名单
        tk.Label(self, text="关键词白名单：").place(x=50, y=260, height=30)
        self.white_list = Text(self, width=20, height=60, undo=True, autoseparators=False)
        self.white_list.place(x=180, y=260, height=60)

        # 开始按钮
        but = tk.Button(self, text="开始", command=partial(self.start), width=20)
        but.place(x=50, y=340, height=30)

        # 停止按钮
        but = tk.Button(self, text="停止", command=partial(self.stop), width=20)
        but.place(x=200, y=340, height=30)

    # 开始刷推荐视频
    def start(self):
        params = {"cycle_index": self.cycle_index.get(), "a_play_time": self.a_play_time.get(),
                  "is_use_ocr": self.is_use_ocr.get(), "black_list": self.black_list.get(1.0, 'end'),
                  "white_list": self.white_list.get(1.0, 'end')}
        print("开始刷推荐视频")
        autoPlay.start(params)

    def stop(self):
        print("停止")
        autoPlay.stop()


class Page2(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack(expand=1, fill="both")
        # 新建文本标签
        labe1 = tk.Label(self, text="账号：")
        # grid()控件布局管理器，以行、列的形式对控件进行布局，后续会做详细介绍
        labe1.grid(row=0)
        # 为上面的文本标签，创建两个输入框控件
        entry1 = tk.Entry(self)
        # 对控件进行布局管理，放在文本标签的后面
        entry1.grid(row=0, column=1)


class Page3(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack(expand=1, fill="both")
        tk.Label(self, text="我是page3").pack()


if __name__ == "__main__":
    root = tk.Tk()
    frame_init(root)
    index = Index(root)
    root.mainloop()
