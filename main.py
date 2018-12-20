# always seem to need this
import sys
 
# For PostgreSQL database 
# import psycopg2

# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread

# for serial communication
import serial
import time
import threading

# This is our window from QtCreator
import mainwindow
import rework

# Windows
mainwin=''
reworkwin=''

# variables
style_on=("font: 75 17pt \"Arial\";\n"+"color: rgb(0, 0, 255);\n"+"background-color: rgb(180, 255, 255);\n"+"border-color: rgb(0, 0, 255);")
style_off=("color: rgb(255, 0, 0);\n"+"font: 75 17pt \"Arial\";\n"+"background-color: rgb(214, 214, 214);")
val_line_active=1
val_of_line=0
ready_setup=0
current_time=0

# components
line_val=''
rework_val=''
val_line23=''
val_line24=''
val_line25=''
val_line26=''
time_lbl=''

# Python threads
valueThread=''

class ValueThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        addValue()

def addValue():
    global current_time,time_lbl
    global val_line_active,val_line23,val_line24,val_line25,val_line26,val_of_line,ready_setup
    while 1:
        if ready_setup ==1:
            val_of_line=val_of_line+1
            if val_line_active == 1:
                val_line23.setText(str(val_of_line))
            elif val_line_active == 2:
                val_line24.setText(str(val_of_line))
            elif val_line_active == 3:
                val_line25.setText(str(val_of_line))
            elif val_line_active == 4:
                val_line26.setText(str(val_of_line))
            current_time=time.localtime( time.time())
            time_now=[0]*3
            time_now[0]=str(current_time.tm_hour)
            time_now[1]=str(current_time.tm_min)
            time_now[2]=str(current_time.tm_sec)
            current_time=''
            for i in range(3):
                if len(time_now[i])==1:
                    time_now[i]='0'+time_now[i]
            current_time=time_now[0]+':'+time_now[1]+':'+time_now[2]
            time_lbl.setText(current_time)
            time.sleep(1)

# create class for our Raspberry Pi GUI
class Rework(QMainWindow, rework.Ui_Form):
    def decrement_val(self):
        global rework_val
        # Decrement rework values
        val=int(rework_val.text())
        if  val > 0:  
            val =  val-1
            rework_val.setText(str(val))

    def increment_val(self):
        global rework_val
        # Increment Rework val
        val=int(rework_val.text())
        if  val < 1000:  
            val =  val+1
            rework_val.setText(str(val))

    def submit_rework(self):
        global rework_val
        val=rework_val.text()
        self.close()

    def __init__(self):
        global line_val,rework_val
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        # Move to the center of window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        # Always on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # Buttons
        self.pb_prev.clicked.connect(self.decrement_val)
        self.pb_next.clicked.connect(self.increment_val)
        self.exit_pb.clicked.connect(self.close)
        self.pb_submit.clicked.connect(self.submit_rework)
        line_val=self.line_val
        rework_val=self.rework_val
        rework_val.setText('0')


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def pb_rework_press(self):
        global reworkwin
        reworkwin.show()

    def pb_line23_pressed(self):
        global val_line23,val_line24,val_line25,val_line26,val_line_active,line_val
        val_line23.setStyleSheet(style_on)
        val_line24.setStyleSheet(style_off)
        val_line25.setStyleSheet(style_off)
        val_line26.setStyleSheet(style_off)
        val_line_active=1
        line_val.setText("Line 23")
    
    def pb_line24_pressed(self):
        global val_line23,val_line24,val_line25,val_line26,val_line_active,line_val
        val_line23.setStyleSheet(style_off)
        val_line24.setStyleSheet(style_on)
        val_line25.setStyleSheet(style_off)
        val_line26.setStyleSheet(style_off)
        val_line_active=2
        line_val.setText("Line 24")

    def pb_line25_pressed(self):
        global val_line23,val_line24,val_line25,val_line26,val_line_active,line_val
        val_line23.setStyleSheet(style_off)
        val_line24.setStyleSheet(style_off)
        val_line25.setStyleSheet(style_on)
        val_line26.setStyleSheet(style_off)
        val_line_active=3
        line_val.setText("Line 25")

    def pb_line26_pressed(self):
        global val_line23,val_line24,val_line25,val_line26,val_line_active,line_val
        val_line23.setStyleSheet(style_off)
        val_line24.setStyleSheet(style_off)
        val_line25.setStyleSheet(style_off)
        val_line26.setStyleSheet(style_on)
        val_line_active=4
        line_val.setText("Line 26")

    def __init__(self):
        global time_lbl
        global val_line23,val_line24,val_line25,val_line26,ready_setup
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        val_line23=self.val_line23
        val_line24=self.val_line24
        val_line25=self.val_line25
        val_line26=self.val_line26
        val_line23.setMargin(20)
        val_line24.setMargin(20)
        val_line25.setMargin(20)
        val_line26.setMargin(20)
        # Initialization of line active on goods detected
        val_line23.setStyleSheet(style_on)
        self.pb_rework.released.connect(self.pb_rework_press)
        self.pb_line23.clicked.connect(self.pb_line23_pressed)
        self.pb_line24.clicked.connect(self.pb_line24_pressed)
        self.pb_line25.clicked.connect(self.pb_line25_pressed)
        self.pb_line26.clicked.connect(self.pb_line26_pressed)
        # label
        time_lbl=self.time_lbl
        # Ready
        ready_setup=1
        
# I feel better having one of these
def main():
    global mainwin,reworkwin
    # a new app instance
    app = QApplication(sys.argv)
    mainwin = MainWindow()
    reworkwin = Rework()
    mainwin.show()
    # reworkwin.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# Create new thread for sending data every second
try:
    valueThread=ValueThread()
except Exception as e:
    print ("Error: unable to start thread!")
    print (str(e))
# Start thread
valueThread.start()

# python bit to figure how who started This
if __name__ == "__main__":
    main()
