# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\dataD\ITS Camp\MATERI LJ\SEMESTER 3\Perancangan dan Integrasi Sistem\Implementasi\HMI-Lakban-Qt5-master\pilih_sumber.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 376)
        Form.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 10, 231, 51))
        self.label.setStyleSheet("color: rgb(255, 170, 0);\n"
"font: 75 28pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 171, 31))
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
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 170, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_pln = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rb_pln.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.rb_pln.setObjectName("rb_pln")
        self.verticalLayout.addWidget(self.rb_pln)
        self.rb_panel = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rb_panel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";\n"
"")
        self.rb_panel.setObjectName("rb_panel")
        self.verticalLayout.addWidget(self.rb_panel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Pilih Sumber"))
        self.label_2.setText(_translate("Form", "Penggunaan :"))
        self.label_3.setText(_translate("Form", "Sumber Listrik :"))
        self.line_val.setText(_translate("Form", "Rumah"))
        self.pb_submit.setText(_translate("Form", "SUBMIT"))
        self.exit_pb.setText(_translate("Form", "x"))
        self.rb_pln.setText(_translate("Form", "PLN"))
        self.rb_panel.setText(_translate("Form", "Panel Surya"))

