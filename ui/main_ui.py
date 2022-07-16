# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
from functools import partial
from main import autoPlay


# 初始化主窗体
def frame_init(window):
    # 设置标题
    root.title("斗音自动助手")
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
        self.pack(expand=1, fill="both")
        lab = tk.Label(self, text="自动刷推荐视频,完播点赞评论功能", font=('宋体', 14))
        lab.grid(row=0, padx=50, pady=15)

        # 开始按钮
        but = tk.Button(self, text="开始", command=partial(self.start), width=30)
        but.grid(row=1, padx=50, pady=15)

        # 停止按钮
        but = tk.Button(self, text="停止", command=partial(self.stop), width=30)
        but.grid(row=2, padx=50, pady=15)

    # 开始刷推荐视频
    def start(self):
        print("开始刷推荐视频")
        autoPlay.start()

    def stop(self):
        print("停止")
        autoPlay.stop()


class Page2(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack(expand=1, fill="both")
        tk.Label(self, text="我是page2").pack()


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

#
# # 创建主窗口
# window = Tk()
# window.title("斗音自动助手")
# # 标题设置

#
#
# # 绑定一个执行函数，当点击菜单项的时候会显示一个消息对话框
# def menuCommand():
#     tkinter.messagebox.showinfo("主菜单栏", "你正在使用主菜单栏")
#

#
# # 调用主事件循环，让窗口程序保持运行。
# window.mainloop()
