from PyQt5 import QtCore, QtGui, QtWidgets
from design import *
import threading
import serial

ser = serial.Serial(
   port='COM11',
   baudrate=115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1)

def Receive_data(self, ui):
    while True:
        rxdata = ser.readline().decode('utf-8')
        if rxdata :
            print(rxdata)

def signals(self):
    self.onButton.clicked.connect(self.ledOn)
    self.offButton.clicked.connect(self.ledOff)

def ledOn(self):
	str='\x02ON\x03\x0a'
	ser.write(bytes(str.encode()))

def ledOff(self):
	str='\x02OFF\x03\x0a'
	ser.write(bytes(str.encode()))

Ui_LED_Control.signals = signals
Ui_LED_Control.ledOn = ledOn
Ui_LED_Control.ledOff = ledOff

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_LED_Control()
    ui.setupUi(Dialog)
    ui.signals()
    thread = threading.Thread(target=Receive_data, args=(ser,ui))
    thread.daemon = True     # 종료시 thread 마침
    thread.start()
    Dialog.show()
    sys.exit(app.exec_())
