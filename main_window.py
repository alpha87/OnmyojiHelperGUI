#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import pythoncom
from threading import Thread
from PyQt5 import QtGui, QtCore, QtWidgets

from good import GoodKey
from DmBase import DmBase
from config import ko_path, win_path


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.pack_all_window()
        self.dm = DmBase()
        self.window_location = self.app_location()

        # --------------------------
        # 御灵之境相关参数

        # 剩余次数
        self.yuling_remainder = 0
        # 判断是否执行完成的标志
        self.yuling_flag = False
        # 攻击次数
        self.yuling_beat_num = 0
        # 进度条数量
        self.yuling_progress_num = 0

    def pack_all_window(self):
        """
        组装所有组件
        """
        self.set_main_window()
        self.set_yuhun_window()
        self.set_yuling_window()
        self.set_tupo_window()
        self.set_log_window()

    def set_main_window(self):
        """
        主窗口配置
        """
        self.setWindowTitle("阴阳师桌面版助手")
        # 隐藏边框
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.resize(260, 270)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QtGui.QIcon("F:\\OnmyojiHelperGUI\\server.ico"))

        # 任务专区
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 161))
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 221, 131))
        self.tabWidget.setObjectName("tabWidget")
        self.groupBox.setTitle("任务专区")

        # 联系作者
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 241, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(150, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2.setTitle("联系作者")
        self.label.setText("jianxun2004@gmail.com")
        self.pushButton.setText("鼓励一下")

        self.pushButton.clicked.connect(self.show_good_key)

    def set_yuling_window(self):
        """
        御灵之境 tab
        """
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setGeometry(QtCore.QRect(60, 10, 61, 21))
        self.spinBox.setObjectName("spinBox")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget.addTab(self.tab_2, "")

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "御灵之境")
        self.label_2.setText("次数：")
        self.pushButton_2.setText("搞起")
        self.label_5.setText("已做随机处理，请放心")

        self.spinBox.valueChanged['int'].connect(self.set_yuling_beat_num)
        self.pushButton_2.clicked.connect(self.yuling_thread_app)

    def set_yuhun_window(self):
        """
        御魂 tab
        """

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox_2.setGeometry(QtCore.QRect(70, 10, 51, 21))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_8 = QtWidgets.QLabel(self.tab_1)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label_8.setObjectName("label_8")
        self.checkBox = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.checkBox.setObjectName("checkBox")
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 31, 21))
        self.label_9.setObjectName("label_9")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_1)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 70, 51, 23))
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_10 = QtWidgets.QLabel(self.tab_1)
        self.label_10.setGeometry(QtCore.QRect(100, 70, 16, 20))
        self.label_10.setObjectName("label_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_4.setGeometry(QtCore.QRect(134, 70, 61, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_1, "")

        self.label_8.setText("刷本次数：")
        self.checkBox.setText("完成后关机")
        self.label_9.setText("剩余")
        self.label_10.setText("次")
        self.pushButton_4.setText("开始")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), "肝御魂")

    def set_tupo_window(self):
        """
        突破 tab
        """

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(11, 10, 36, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 84, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 84, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 84, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.label_3.setText("注意：")
        self.label_4.setText("1.随机选择结界")
        self.label_6.setText("2.充足的突破券")
        self.label_7.setText("3.完整的九宫格")
        self.pushButton_3.setText("突破")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "结界突破")

    def set_log_window(self):
        """
        日志 tab
        """

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(9, 9, 201, 91))
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.tabWidget.addTab(self.tab_4, "")

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), "日志")

    @staticmethod
    def show_good_key():
        """
        展示赞赏码
        """
        ui = GoodKey()
        MainWindow = QtWidgets.QDialog()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()

    def app_location(self):
        """
        获取前台坐标，并把窗口改为默认大小
        """
        hwnd = self.dm.find_windows("阴阳师-网易游戏")
        self.dm.set_window_size(hwnd)
        return self.dm.get_client_rect(hwnd)

    # --------------------------
    # 御灵之境

    @property
    def weekday(self):
        """
        返回当天星期
        """
        return time.strftime("%A")

    def get_pic(self, path, location):
        """
        找图
        """
        kwargs = {
            "left": location[1],
            "top": location[2],
            "right": location[3],
            "down": location[4],
            "pic_path": path,
            "sim": 0.8,
            "dir": 0
        }
        pic_path = self.dm.find_pic_e(**kwargs)
        x, y = pic_path.split("|")[1:]
        return x, y

    def beat_one(self, peo):
        if not self.yuling_flag:
            rx = random.randint(-20, 20)
            ry = random.randint(1, 50)
            self.dm.move_to(peo[0], peo[1], x=rx, y=ry)
            time.sleep(1)
            self.dm.left_click()
        print("准备挑战...")
        self.plainTextEdit_2.insertPlainText("准备挑战...\n")
        time.sleep(random.randint(2, 5))
        x, y = self.get_pic(ko_path, self.window_location)

        if x != "-1" and y != "-1":
            self.dm.move_to(x, y, x=random.randint(1, 10), y=random.randint(1, 5))
            self.dm.left_click()
            print("开始")
            self.plainTextEdit_2.insertPlainText("开始\n")

        while True:
            print("等待结果...")
            self.plainTextEdit_2.insertPlainText("等待结果...\n")
            yuling_flag = self.find_win_button(self.window_location)
            if yuling_flag:
                break
            time.sleep(8)

    def find_win_button(self, windows_location):
        x, y = self.get_pic(path=win_path, location=windows_location)
        if x != "-1" and y != "-1":
            print("已胜利！")
            self.dm.move_to(x, y, x=random.randint(1, 5), y=random.randint(1, 5))
            self.dm.left_click()
            time.sleep(5)
            return True
        return False

    def yuling_app(self, num):
        """
        御灵程序主入口
        """
        windows_location = self.app_location()
        left = windows_location[1]
        top = windows_location[2]

        # 九个挑战目标
        peo1 = left + 215, top + 355
        peo2 = left + 455, top + 360
        peo3 = left + 690, top + 370
        peo4 = left + 935, top + 365

        item = None
        if self.weekday == "Tuesday":
            item = peo1
        elif self.weekday == "Wednesday":
            item = peo2
        elif self.weekday == "Thursday":
            item = peo3
        elif self.weekday == "Friday":
            item = peo4
        elif self.weekday == "Monday":
            print("周一没得打啊！")
        else:
            item = peo1
        i = 0
        while i < int(num):
            self.set_yuling_progress_num()
            print(f"进度条已进行 {self.yuling_progress_num}")
            self.plainTextEdit_2.insertPlainText(f"进度条已进行 {self.yuling_progress_num}\n")
            self.progressBar.setValue(self.yuling_progress_num)
            self.beat_one(item)
            self.yuling_flag = True
            time.sleep(random.randint(3, 8))
            i += 1
            self.yuling_remainder = int(num) - 1
        print("已经完成任务")
        self.plainTextEdit_2.insertPlainText("已经完成任务\n")

    def set_yuling_beat_num(self, num):
        """
        设定御灵之境攻击次数
        """
        self.yuling_beat_num = int(num)
        print(f"御灵之境攻击次数为{self.yuling_beat_num}次")

    def set_yuling_progress_num(self):
        """
        计算御灵之境进度条
        """
        self.yuling_progress_num += 100 / self.yuling_beat_num

    def yuling_thread_app(self):
        thr = Thread(target=self.yuling_run)
        thr.setDaemon(True)
        thr.start()

    def yuling_run(self):
        pythoncom.CoInitialize()
        self.yuling_app(self.yuling_beat_num)

    # --------------------------
    # 御魂


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())
