from my import*
import PyQt5
from functools import partial
import time
import threading
import datetime
import requests
from PyQt5.QtCore import pyqtSignal
import sqlite3


class EventThread(PyQt5.QtCore.QThread):

    def __init__(self, ui):
        self.mainButton_list = [ui.btn_main_off, ui.btn_graph_off, ui.btn_setting]
        for i, mainButton in enumerate(self.mainButton_list):
            mainButton.clicked.connect(partial(ui.stackedWidget.setCurrentIndex, i))


class comboBoxChange:

    def fan(self):
        data = ui.comboBox_fan.currentText()
        if data == 'Manual':
            print('선풍기 수동 모드')
        else:
            print('선풍기 자동 모드')

    def led(self):
        data = ui.comboBox_led.currentText()
        if data == 'Manual':
            print('LED 밝기 수동 모드')
        else:
            print('LED 밝기 자동 모드')

    def water(self):
        data = ui.comboBox_water.currentText()
        if data == 'Manual':
            print('물 주기 수동 모드')
        else:
            print('물 주기 자동 모드')

    def picture(self):
        data = ui.comboBox_picture.currentText()
        if data == 'Manual':
            print('사진 촬영 수동 모드')
        else:
            print('사진 촬영 자동 모드')


class date_time:
    def change_time(ui):
        while True:
            date = datetime.datetime.now()
            date = date.strftime('%H:%M:%S')
            ui.label_time.setText(date)
            time.sleep(1)


    def change_date(ui):
        while True:
            date1 = datetime.datetime.now()
            date1 = date1.strftime('%Y-%m-%d')
            ui.label_29.setText(date1)
            time.sleep(1)


class sensor:
    def sensor_date(ui):
        url = 'http://10.156.147.138:5000/'

        while True:
            res = requests.get(url=url)
            data = res.text
            temp = data[2:7]
            humid = data[9:14]
            ui.label_temp.setText(temp)
            ui.label_humid.setText(humid)
            dt = datetime.datetime.now()
            time_text = dt.strftime("%H:%M:%S")
            date_text = dt.strftime("%Y-%m-%d")

            con = sqlite3.connect('./db_data/main.db')
            cur = con.cursor()
            cur.execute("CREATE TABLE if not exists SensorData(Date text, Time text, Temp text, Humid text);")
            cur.execute(f'INSERT INTO SensorData VALUES("{date_text}", "{time_text}", "{temp}", "{humid}");')
            con.commit()
            cur.execute("SELECT * FROM SensorData;")
            con.close()
            time.sleep(3)


def signals(ui):
    ui.comboBox_fan.currentIndexChanged.connect(comboBoxChange.fan)
    ui.comboBox_water.currentIndexChanged.connect(comboBoxChange.water)
    ui.comboBox_led.currentIndexChanged.connect(comboBoxChange.led)
    ui.comboBox_picture.currentIndexChanged.connect(comboBoxChange.picture)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    signals(ui)

    eventThread = EventThread(ui)
    thread1 = threading.Thread(target=date_time.change_time, args=(ui,))
    thread1.daemon = True
    thread1.start()
    thread2 = threading.Thread(target=date_time.change_date, args=(ui,))
    thread2.daemon = True
    thread2.start()
    thread3= threading.Thread(target=sensor.sensor_date, args=(ui,))
    thread3.daemon = True
    thread3.start()

    sys.exit(app.exec_())