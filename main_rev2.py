# Note : 
# always seem to need this
import sys
 
# For PostgreSQL database 
# import psycopg2

# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
from PyQt5.QtGui import QPixmap

# for serial communication
import serial
import time
import threading

# This is our window from QtCreator
import mainwindow_rev2
import rework
import popup
import pilih_sumber

import RPi.GPIO as GPIO

# Indicator pin initialization
lamp1_pin=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(lamp1_pin, GPIO.OUT)
GPIO.output(lamp1_pin, 1)

lamp2_pin=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(lamp2_pin, GPIO.OUT)
GPIO.output(lamp2_pin, 1)

lamp3_pin=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(lamp3_pin, GPIO.OUT)
GPIO.output(lamp3_pin, 1)

# Change Source
source_pln=8
GPIO.setmode(GPIO.BCM)
GPIO.setup(source_pln, GPIO.OUT)
GPIO.output(source_pln, 1)

source_panel=7
GPIO.setmode(GPIO.BCM)
GPIO.setup(source_panel, GPIO.OUT)
GPIO.output(source_panel, 1)

print("source PLN")
GPIO.output(source_pln, 0)
GPIO.output(source_panel, 1)

# Windows
mainwin=''
reworkwin=''
popupwin=''
pilihsumber=''

# variables
style_on=("font: 75 30pt \"Arial\";\n"+"color: rgb(0, 0, 255);\n"+"background-color: rgb(180, 255, 255);\n"+"border-color: rgb(0, 0, 255);")
style_off=("color: rgb(255, 0, 0);\n"+"font: 75 30pt \"Arial\";\n"+"background-color: rgb(214, 214, 214);")
val_line_active=1
val_of_line=0
ready_setup=0
current_time=0
popupSignalStop=''
startPopup=0
source=""
lamp1_toggle=0
lamp2_toggle=0
lamp3_toggle=0

# components
line_val=''
rework_val=''
val_line23=''
time_lbl=''
popup_text=''
lbl_source=''
lbl_daya=''
lamp1_indicator=''
lamp2_indicator=''
lamp3_indicator=''

# Python threads
valueThread=''
popupThread=''

## Establish connection to COM Port
## Connection from HMI
print ("Connecting...")
connected=False
ser_to_hmi='null'
buff=''
locations=['/dev/ttyAMA0']
locations=['serial0']
## COM Port settings
for device in locations: 
    try:
        print ("Trying...",device)
        ## Serial Initialization
        ser_to_hmi = serial.Serial(device,      #port
                            115200
                            # ,              #baudrate
                            # serial.EIGHTBITS,   #bytesize
                            # serial.PARITY_ODD,  #parity
                            # serial.STOPBITS_ONE,#stop bit
                            # 0,                  #timeout
                            # False,              #xonxoff
                            # False,              #rtscts
                            # 0,                  #write_timeout
                            # False,              #dsrdtr
                            # None,               #inter byte timeout
                            # None                #exclusive
                            )
        connected=True
        break
    except:
        print ("Failed to connect on ", device)

# ## loop until the device tells us it is ready
# while not connected:
#     serin = ser_to_hmi.read()
#     connected = True
# print ("Connected to ",device)
# connected=False


class PopupThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        popupRun()

def popupRun():
    global popupSignalStop,startPopup
    while 1:
        if startPopup==1:
            time.sleep(3)
            if startPopup == 1:
                popupSignalStop.emit()                

class ValueThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        # addValue()
        getCurrent()

def getCurrent():
    global ser_to_hmi, buff, lbl_daya
    print("Get Serial data")
    while 1:
        if(ser_to_hmi!="null"):
            # Waiting data from HMI
            if ser_to_hmi.inWaiting():
                x=ser_to_hmi.read()
                buff=buff + x
                print(x)
                if x == '\r':
                    # print "data from HMI :"
                    print (buff)
                    lbl_daya.setText(str(buff))
                    buff=''
        # time.sleep(1)

def addValue():
    global current_time,time_lbl
    global val_line23,val_of_line,ready_setup
    while 1:
        if ready_setup ==1:
            val_of_line=val_of_line+1
            # val_line23.setText(str(val_of_line))

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

class pilihSumber(QMainWindow, pilih_sumber.Ui_Form):
    def submit_sumber(self):
        global lbl_source, source
        lbl_source.setText(source)
        # Change Source (PLN or Panel)
        if(source=="PLN"):
            # Switch to PLN source
            print("source PLN")
            GPIO.output(source_pln, 0)
            GPIO.output(source_panel, 1)
        elif(source=="PANEL"):
            # Switch to Panel Source
            print("source Panel")
            GPIO.output(source_pln, 1)
            GPIO.output(source_panel, 0)
        self.close()

    def btnstate_pln(self, rb_pln):
        global source
        if rb_pln.isChecked() == True:
            source="PLN"
            print("PLN")

    def btnstate_panel(self, rb_panel):
        global source
        if rb_panel.isChecked() == True:
            source="PANEL"
            print("PANEL")

    def __init__(self):
        global source
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        # Move to the center of window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        # Always on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.exit_pb.clicked.connect(self.close)
        self.pb_submit.clicked.connect(self.submit_sumber)
        self.rb_pln.setChecked(True)
        self.rb_panel.setChecked(False)
        source="PLN"
        self.rb_pln.toggled.connect(lambda:self.btnstate_pln(self.rb_pln))
        self.rb_panel.toggled.connect(lambda:self.btnstate_panel(self.rb_panel))

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
        global rework_val,val_line23,val_of_line,popupwin,startPopup
        val=rework_val.text()
        print(val)
        current_val=int(val_line23.text())
        # Substract current value by rework value
        current_val=current_val-int(val)
        print(current_val)
        val_of_line=current_val
        self.close()
        popupwin.show()
        startPopup=1

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
class MainWindow(QMainWindow, mainwindow_rev2.Ui_MainWindow):
    def pb_rework_press(self):
        pass
        #global reworkwin
        # reworkwin.show()
        # GPIO.output(indicator_pin, 1)
    def pb_rework_release(self):
        # GPIO.output(indicator_pin, 0)
        pass

    def pb_sources_release(self):
        global pilihsumber
        pilihsumber.show()

    def pb_lamp1_release(self):
        global lamp1_indicator, lamp1_toggle
        if (lamp1_toggle==0):
            lamp1_toggle=1
            # Turn on Lamp1
            GPIO.output(lamp1_pin, 0)
            lamp1_indicator.setPixmap(QPixmap("/home/pi/Smart-Home-Project/light.png"))
            # lamp1_indicator.setPixmap(QPixmap("light.png"))
        elif (lamp1_toggle==1):
            lamp1_toggle=0
            # Turn off Lamp1
            GPIO.output(lamp1_pin, 1)
            lamp1_indicator.setPixmap(QPixmap("/home/pi/Smart-Home-Project/dark.png"))
            # lamp1_indicator.setPixmap(QPixmap("dark.png"))

        # Change lamp resources
    def pb_lamp2_release(self):
        global lamp2_indicator, lamp2_toggle
        if (lamp2_toggle==0):
            lamp2_toggle=1
            # Turn on Lamp2
            GPIO.output(lamp2_pin, 0)
            lamp2_indicator.setPixmap(QPixmap("/home/pi/Smart-Home-Project/light.png"))
            # lamp2_indicator.setPixmap(QPixmap("light.png"))
        elif (lamp2_toggle==1):
            lamp2_toggle=0
            # Turn off Lamp2
            GPIO.output(lamp2_pin, 1)
            lamp2_indicator.setPixmap(QPixmap("/home/pi/Smart-Home-Project/dark.png"))
            # lamp2_indicator.setPixmap(QPixmap("dark.png"))

    # def pb_lamp3_release(self):
    #     global lamp3_indicator, lamp3_toggle
    #     if (lamp3_toggle==0):
    #         lamp3_toggle=1
    #         # Turn on Lamp3
    #         GPIO.output(lamp3_pin, 0)
    #         lamp3_indicator.setPixmap(QPixmap("/home/pi/Smart-Home-Project/light.png"))
    #         # lamp3_indicator.setPixmap(QPixmap("light.png"))
    #     elif (lamp3_toggle==1):
    #         lamp3_toggle=0
    #         # Turn off Lamp3
    #         GPIO.output(lamp3_pin, 1)
    #         lamp3_indicator.setPixmap(QPixmap("/home/pi/Smart-Home-Project/dark.png"))
    #         # lamp3_indicator.setPixmap(QPixmap("dark.png"))

    def __init__(self):
        global time_lbl, lbl_source, lamp1_indicator, lamp2_indicator, lamp3_indicator
        global val_line23,ready_setup, lbl_daya
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        # val_line23=self.val_line23
        # val_line23.setMargin(20)
        # Initialization of line active on goods detected
        # val_line23.setStyleSheet(style_on)
        self.pb_lamp1.pressed.connect(self.pb_rework_press)

        self.pb_lamp1.released.connect(self.pb_lamp1_release)
        self.pb_lamp2.released.connect(self.pb_lamp2_release)
        # self.pb_lamp3.released.connect(self.pb_lamp3_release)

        # Lamp Indicator
        lamp1_indicator=self.lamp1_indicator
        lamp2_indicator=self.lamp2_indicator
        # lamp3_indicator=self.lamp3_indicator
        lamp1_indicator.setPixmap(QPixmap("/home/pi/Smart-Home-Project/dark.png"))
        lamp2_indicator.setPixmap(QPixmap("/home/pi/Smart-Home-Project/dark.png"))
        # lamp3_indicator.setPixmap(QPixmap("/home/pi/Smart-Home-Project/dark.png"))

        self.pb_sources.released.connect(self.pb_sources_release)
        lbl_source=self.lbl_source
        lbl_daya=self.lbl_daya
        # label
        time_lbl=self.time_lbl
        # Ready
        ready_setup=1

# create class for our Raspberry Pi GUI
class Popup(QMainWindow, popup.Ui_Form):
    popupSignalStop = pyqtSignal(name='popupSignalStop')

    def sendPopupSignalStop(self):
        global startPopup
        self.close()
        startPopup=0

    def closePressed(self, event):
        global startPopup
        self.close()
        startPopup=0

    def __init__(self):
        global popup_text,popupSignalStop
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        # Move to the center of window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        popup_text=self.popup_text
        self.lbl_close.mousePressEvent=self.closePressed

        # Create Qt signal to emit minor stop signal
        popupSignalStop=self.popupSignalStop
        popupSignalStop.connect(self.sendPopupSignalStop)

        
# I feel better having one of these
def main():
    global mainwin,reworkwin,popupwin,pilihsumber
    # a new app instance
    app = QApplication(sys.argv)
    mainwin = MainWindow()
    reworkwin = Rework()
    popupwin = Popup()
    pilihsumber = pilihSumber()
    mainwin.show()
    # reworkwin.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# Create new thread for sending data every second
try:
    valueThread=ValueThread()
    popupThread=PopupThread()
except Exception as e:
    print ("Error: unable to start thread!")
    print (str(e))
# Start thread
valueThread.start()
popupThread.start()

# python bit to figure how who started This
if __name__ == "__main__":
    main()
