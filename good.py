#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class GoodKey(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(458, 505)
        Form.setWindowIcon(QtGui.QIcon("F:\\OnmyojiHelperGUI\\good.ico"))
        # Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(-220, -130, 901, 941))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("F:\\OnmyojiHelperGUI\\picture\\q16.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(143, 431, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "鼓励作者"))
        self.label.setText(_translate("Form", "好人一生平安"))
