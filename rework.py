# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Qt/Qt5-HMI-test/rework.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 376)
        Form.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 10, 191, 51))
        self.label.setStyleSheet("color: rgb(255, 170, 0);\n"
"font: 75 28pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 81, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 175, 221, 61))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.line_val = QtWidgets.QLabel(Form)
        self.line_val.setGeometry(QtCore.QRect(340, 100, 161, 41))
        self.line_val.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(236, 236, 236);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.line_val.setAlignment(QtCore.Qt.AlignCenter)
        self.line_val.setObjectName("line_val")
        self.pb_submit = QtWidgets.QPushButton(Form)
        self.pb_submit.setGeometry(QtCore.QRect(0, 280, 611, 101))
        self.pb_submit.setStyleSheet("font: 75 28pt \"Arial\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pb_submit.setObjectName("pb_submit")
        self.exit_pb = QtWidgets.QPushButton(Form)
        self.exit_pb.setGeometry(QtCore.QRect(540, 10, 50, 41))
        self.exit_pb.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(243, 0, 0);\n"
"font: 75 28pt \"Arial\";")
        self.exit_pb.setObjectName("exit_pb")
        self.horizontalWidget = QtWidgets.QWidget(Form)
        self.horizontalWidget.setGeometry(QtCore.QRect(300, 160, 244, 80))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_prev = QtWidgets.QPushButton(self.horizontalWidget)
        self.pb_prev.setMinimumSize(QtCore.QSize(0, 50))
        self.pb_prev.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);\n"
"font: 75 24pt \"Arial\";")
        self.pb_prev.setObjectName("pb_prev")
        self.horizontalLayout.addWidget(self.pb_prev)
        self.rework_val = QtWidgets.QLabel(self.horizontalWidget)
        self.rework_val.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Arial\";")
        self.rework_val.setAlignment(QtCore.Qt.AlignCenter)
        self.rework_val.setObjectName("rework_val")
        self.horizontalLayout.addWidget(self.rework_val, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pb_next = QtWidgets.QPushButton(self.horizontalWidget)
        self.pb_next.setMinimumSize(QtCore.QSize(0, 50))
        self.pb_next.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);\n"
"font: 75 24pt \"Arial\";")
        self.pb_next.setObjectName("pb_next")
        self.horizontalLayout.addWidget(self.pb_next)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "REWORK"))
        self.label_2.setText(_translate("Form", "Line :"))
        self.label_3.setText(_translate("Form", "Jumlah Rework :"))
        self.line_val.setText(_translate("Form", "Line 23"))
        self.pb_submit.setText(_translate("Form", "SUBMIT"))
        self.exit_pb.setText(_translate("Form", "x"))
        self.pb_prev.setText(_translate("Form", "<<"))
        self.rework_val.setText(_translate("Form", "1000"))
        self.pb_next.setText(_translate("Form", ">>"))

