#!/usr/bin/env python
# -*- coding: utf-8 -*-
import win32com.client
from config import dict_path


class DmBase(object):

    __doc__ = """封装大漠插件部分方法"""

    def __init__(self):
        self.dm = win32com.client.Dispatch("dm.dmsoft")
        self.dm.setDict(0, dict_path)
        self.dm.useDict(0)

    def find_windows(self, handle):
        """
        查找客户端对应句柄
        """
        return self.dm.FindWindow("", handle)

    def bind_windows(self, handle):
        """
        默认前台客户端, 模拟鼠标操作

        display 字符串: 屏幕颜色获取方式 取值有以下几种
        "normal" : 正常模式,平常我们用的前台截屏模式
        "gdi" : gdi模式,用于窗口采用GDI方式刷新时. 此模式占用CPU较大.
        "gdi2" : gdi2模式,此模式兼容性较强,但是速度比gdi模式要慢许多,如果gdi模式发现后台不刷新时,可以考虑用gdi2模式.
        "dx2" : dx2模式,用于窗口采用dx模式刷新,如果dx方式会出现窗口所在进程崩溃的状况,可以考虑采用这种.采用这种方式要保证窗口有一部分在屏幕外.win7或者vista不需要移动也可后台.此模式占用CPU较大.
        "dx3" : dx3模式,同dx2模式,但是如果发现有些窗口后台不刷新时,可以考虑用dx3模式,此模式比dx2模式慢许多. 此模式占用CPU较大.
        "dx" : dx模式,等同于BindWindowEx中，display设置的"dx.graphic.2d|dx.graphic.3d",具体参考BindWindowEx
        """
        return self.dm.BindWindow(handle, "normal", "windows", "windows", 1)

    def get_client_rect(self, handle):
        """
        查找句柄对应坐标
        """
        return self.dm.GetClientRect(handle)

    def find_pic_e(self, **kwargs):
        """
        区域找图
        FindPicE(x1, y1, x2, y2, pic_name, delta_color,sim, dir)

        x1 整形数:区域的左上X坐标
        y1 整形数:区域的左上Y坐标
        x2 整形数:区域的右下X坐标
        y2 整形数:区域的右下Y坐标
        pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
        delta_color 字符串:颜色色偏比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示)
        sim 双精度浮点数:相似度,取值范围0.1-1.0
        dir 整形数:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
        """
        return self.dm.FindPicE(kwargs.get("left"),
                                kwargs.get("top"),
                                kwargs.get("right"),
                                kwargs.get("down"),
                                kwargs.get("pic_path"),
                                "000000",
                                kwargs.get("sim"),
                                kwargs.get("dir"))

    def move_to(self, X, Y, x=0, y=0):
        """
        移动鼠标

        :param X: x
        :param Y: y
        :param x: 偏移量
        :param y: 偏移量
        """
        return self.dm.MoveTo(str(int(X)+x), str(int(Y)+y))

    def left_click(self):
        """
        单击左键
        """
        return self.dm.LeftClick()

    def capture_pic(self, x1, y1, x2, y2, file_name, quality=50):
        """
        抓取指定区域保存为jpg
        quality 范围：1~100
        """
        self.dm.CaptureJpg(x1, y1, x2, y2, file_name, quality)

    def ocr(self, x1, y1, x2, y2, color_format, sim=0.9):
        """
        文字识别

        x1 整形数:区域的左上X坐标
        y1 整形数:区域的左上Y坐标
        x2 整形数:区域的右下X坐标
        y2 整形数:区域的右下Y坐标
        color_format 字符串:颜色格式串. 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV格式都支持.
        sim 双精度浮点数:相似度,取值范围0.1-1.0

        返回值:
        返回识别到的字符串
        """
        return self.dm.Ocr(x1, y1, x2, y2, color_format, sim)

    def set_window_size(self, handle):
        """
        设置窗口大小
        窗口默认大小为 1136,640
        """
        return self.dm.SetClientSize(handle, 1136, 640)


if __name__ == '__main__':
    dm = DmBase()
    hwnd = dm.find_windows("阴阳师-网易游戏")
    dm.set_window_size(hwnd)
