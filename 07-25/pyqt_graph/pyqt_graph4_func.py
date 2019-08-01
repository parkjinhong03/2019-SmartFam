from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt_graph4 import *
import pyqtgraph as pg
import threading
import serial
import numpy as numpy
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

temperature=[]
humidity=[]
cotwo=[]

Now_temp=0
Now_humi=0
Now_cotwo=0

ser = serial.Serial(port='COM11',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)


def Receive_data(self, ui):
    global Now_temp, Now_humi, Now_cotwo
    cnt=0
    while True:
        rxdata = ser.readline().decode('utf-8')
        if rxdata :
            print(rxdata)
            temp=rxdata[2:7]
            tempf=float(temp)
            temperature.append(tempf)
            Now_temp=tempf

            humi=rxdata[9:13]
            humif=float(humi)
            humidity.append(humif)
            Now_humi=humif

            co2=rxdata[16:]
            co2i=int(co2)
            cotwo.append(co2i)
            Now_cotwo=co2i

            cnt=cnt+1
            if(cnt>20):
                temperature.pop(0)
                humidity.pop(0)
                cotwo.pop(0)
                cnt = 21

            ui.uiUpdateDelegate.emit(1)

class MyFirstGuiProgram(QtWidgets.QMainWindow, Ui_Dialog):
    global Now_temp, Now_humi, Now_cotwo
    uiUpdateDelegate = pyqtSignal(int)
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.uiUpdateDelegate.connect(self.uiUpdater)
        self.graphicsView.setBackground('#ffffff')
        self.graphicsView.setRange(xRange=[2, 20])
        self.graphicsView.showGrid(x=True, y=True)
    def uiUpdater(self):
        self.graphicsView.clear()
        self.graphicsView.plot(temperature, pen=pg.mkPen('r', width=2),
            style=QtCore.Qt.DashLine, symbol=('o'), symbolBrush='r', symbolSize=5)
        self.graphicsView.plot(humidity, pen=pg.mkPen('b', width=2),
            style=QtCore.Qt.DashLine, symbol=('x'),  symbolBrush='b')
        self.graphicsView.plot(cotwo, pen=pg.mkPen('g', width=2),
            style=QtCore.Qt.DashLine, symbol=('t1'),   symbolBrush='g')

        self.DisTemp.setText(str(Now_temp))
        self.DisHumi.setText(str(Now_humi))
        self.DisCo2.setText(str(Now_cotwo))

    def update_sensor(self):
        str='sZ\x0a'
        ser.write(bytes(str.encode()))
        QTimer.singleShot(1000, self.update_sensor)


def signals(self):
    self.Quit.clicked.connect(self.quit)


def quit(self):
    print('Quit Program')


Ui_Dialog.signals = signals
Ui_Dialog.quit = quit

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = MyFirstGuiProgram()
    ui.show()
    ui.signals()
    thread = threading.Thread(target=Receive_data, args=(ser, ui))
    thread.daemon = True
    thread.start()
    QTimer.singleShot(1000, ui.update_sensor)
    sys.exit(app.exec_())

