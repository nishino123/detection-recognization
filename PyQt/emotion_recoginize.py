# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emotion_recoginize.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(951, 579)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 370, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 330, 311, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(340, 30, 16, 471))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_emotion = QtWidgets.QLabel(Form)
        self.label_emotion.setGeometry(QtCore.QRect(360, 30, 54, 12))
        self.label_emotion.setObjectName("label_emotion")
        self.label_raw_pic = QtWidgets.QLabel(Form)
        self.label_raw_pic.setGeometry(QtCore.QRect(10, 30, 320, 238))
        self.label_raw_pic.setStyleSheet("background-color:#bbbbbb;")
        self.label_raw_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_raw_pic.setObjectName("label_raw_pic")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(360, 200, 561, 341))
        self.graphicsView.setObjectName("graphicsView")
        self.label_rst = QtWidgets.QLabel(Form)
        self.label_rst.setGeometry(QtCore.QRect(510, 70, 161, 91))
        self.label_rst.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rst.setObjectName("label_rst")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(370, 160, 531, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.select)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "选择图像"))
        self.label_emotion.setText(_translate("Form", "识别结果"))
        self.label_raw_pic.setText(_translate("Form", "O(∩_∩)O"))
        self.label_rst.setText(_translate("Form", "Result"))

