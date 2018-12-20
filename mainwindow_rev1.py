# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Qt\HMI-Lakban-Qt5\mainwindow_rev1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(570, 20, 201, 41))
        self.label_9.setStyleSheet("font: 75 18pt \"Arial\";\n"
"color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 255);")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(30, 150, 521, 41))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 40))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"background-color: rgb(0, 0, 131);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.gridGroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.gridGroupBox.setGeometry(QtCore.QRect(30, 210, 521, 241))
        self.gridGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.val_line23 = QtWidgets.QLabel(self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_line23.sizePolicy().hasHeightForWidth())
        self.val_line23.setSizePolicy(sizePolicy)
        self.val_line23.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 30pt \"Arial\";\n"
"background-color: rgb(214, 214, 214);")
        self.val_line23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.val_line23.setAlignment(QtCore.Qt.AlignCenter)
        self.val_line23.setWordWrap(False)
        self.val_line23.setObjectName("val_line23")
        self.gridLayout.addWidget(self.val_line23, 0, 0, 1, 1)
        self.horizontalWidget1 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalWidget1.setGeometry(QtCore.QRect(30, 20, 221, 41))
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time_lbl = QtWidgets.QLabel(self.horizontalWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.time_lbl.setFont(font)
        self.time_lbl.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 22pt \"Arial\";")
        self.time_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.time_lbl.setObjectName("time_lbl")
        self.horizontalLayout.addWidget(self.time_lbl)
        self.label = QtWidgets.QLabel(self.horizontalWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.shift_lbl = QtWidgets.QLabel(self.horizontalWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.shift_lbl.setFont(font)
        self.shift_lbl.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 22pt \"Arial\";")
        self.shift_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.shift_lbl.setObjectName("shift_lbl")
        self.horizontalLayout.addWidget(self.shift_lbl)

        self.pb_rework = QtWidgets.QPushButton(self.centralWidget)
        self.pb_rework.setGeometry(QtCore.QRect(570, 80, 151, 50))
        self.pb_rework.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 24pt \"Arial\";")
        self.pb_rework.setObjectName("pb_rework")

        self.pb_lamp2 = QtWidgets.QPushButton(self.centralWidget)
        self.pb_lamp2.setGeometry(QtCore.QRect(570, 140, 151, 50))
        self.pb_lamp2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 24pt \"Arial\";")
        self.pb_lamp2.setObjectName("pb_lamp2")

        self.pb_lamp3 = QtWidgets.QPushButton(self.centralWidget)
        self.pb_lamp3.setGeometry(QtCore.QRect(570, 200, 151, 50))
        self.pb_lamp3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 24pt \"Arial\";")
        self.pb_lamp3.setObjectName("pb_lamp3")

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 521, 61))
        self.label_2.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"font: 75 28pt \"Arial\";")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Lamp Switch"))
        self.label_10.setText(_translate("MainWindow", "Total Daya (Watt)"))
        self.val_line23.setText(_translate("MainWindow", "0"))
        self.time_lbl.setText(_translate("MainWindow", "09:45:55"))
        self.label.setText(_translate("MainWindow", "|"))
        self.shift_lbl.setText(_translate("MainWindow", "House 1"))
        self.pb_rework.setText(_translate("MainWindow", "Lamp 1"))
        self.pb_lamp2.setText(_translate("MainWindow", "Lamp 2"))
        self.pb_lamp3.setText(_translate("MainWindow", "Lamp 3"))
        self.label_2.setText(_translate("Mainindow", "Room 1"))

