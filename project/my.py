# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 474)
        MainWindow.setStyleSheet("QDockWidget {\n"
"    border: 1px solid lightgray;\n"
"    titlebar-close-icon: url(close.png);\n"
"    titlebar-normal-icon: url(undock.png);\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    text-align: left; /* align the text to the left */\n"
"    background: lightgray;\n"
"    padding-left: 5px;\n"
"}    ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 221, 471))
        self.label_3.setStyleSheet("background-color: #bbf0ee;\n"
"border: 1px solid black;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.btn_main_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_main_on.setGeometry(QtCore.QRect(370, 86, 85, 31))
        self.btn_main_on.setStyleSheet("background-color: rgba(0, 0, 0, 170);\n"
"color: white;\n"
"font: 15px;\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"font-weight: bold;\n"
"")
        self.btn_main_on.setObjectName("btn_main_on")
        self.btn_graph_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_graph_off.setGeometry(QtCore.QRect(481, 86, 85, 31))
        self.btn_graph_off.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255, 150);\n"
"color: black;\n"
"font: 15px;\n"
"font-weight: bold;\n"
"border-radius: 15px;\n"
"border: 1px solid black;}\n"
"QPushButton:hover{background-color: rgb(179, 179, 179, 150);\n"
"color: black;\n"
"font: 15px;\n"
"font-weight: bold;\n"
"border-radius: 15px;\n"
"border: 1px solid black;}\n"
"")
        self.btn_graph_off.setObjectName("btn_graph_off")
        self.btn_setting = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setting.setGeometry(QtCore.QRect(590, 86, 85, 31))
        self.btn_setting.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255, 150);\n"
"color: black;\n"
"font: 15px;\n"
"font-weight: bold;\n"
"border-radius: 15px;\n"
"border: 1px solid black;}\n"
"QPushButton:hover{background-color: rgb(179, 179, 179, 150);\n"
"color: black;\n"
"font: 15px;\n"
"font-weight: bold;\n"
"border-radius: 15px;\n"
"border: 1px solid black;}\n"
"")
        self.btn_setting.setObjectName("btn_setting")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(540, 10, 131, 51))
        self.label_26.setStyleSheet("font: 55px Bahnschrift;\n"
"color: green;")
        self.label_26.setObjectName("label_26")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(14, 40, 191, 110))
        self.label_date.setStyleSheet("border-radius: 20px;\n"
"border: 1px solid black;")
        self.label_date.setText("")
        self.label_date.setObjectName("label_date")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(20, 90, 181, 41))
        self.label_time.setStyleSheet("color: black;\n"
"font: 50px Bahnschrift;")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(55, 60, 121, 21))
        self.label_29.setStyleSheet("color: black;\n"
"font: 20px;\n"
"font-weight: bold;")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(50, 155, 121, 41))
        self.label_30.setStyleSheet("font: 40px Bahnschrift;\n"
"font-weight: bold;\n"
"color: black;\n"
"background-color:#bbf0ee;")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(10, 180, 201, 271))
        self.label_31.setStyleSheet("border-radius: 20px;\n"
"border: 1px solid black;")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(65, 15, 91, 41))
        self.label_33.setStyleSheet("font: 40px Bahnschrift;\n"
"font-weight: bold;\n"
"color: black;\n"
"background-color:#bbf0ee;")
        self.label_33.setObjectName("label_33")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(370, 10, 191, 51))
        self.label_27.setStyleSheet("font: 55px Bahnschrift;\n"
"color: black;")
        self.label_27.setObjectName("label_27")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 210, 71, 71))
        self.label_14.setStyleSheet("border-image: url(:/img/led.jpg);\n"
"border-radius: 35px;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.comboBox_led = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_led.setGeometry(QtCore.QRect(30, 290, 71, 21))
        self.comboBox_led.setStyleSheet("border-radius: 20px;\n"
"border: 1px inset black; \n"
"background-color: #bbf0ee;\n"
"font: 15px Bahnschrift;\n"
"text-align: center;")
        self.comboBox_led.setObjectName("comboBox_led")
        self.comboBox_led.addItem("")
        self.comboBox_led.addItem("")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(120, 210, 71, 71))
        self.label_16.setStyleSheet("border-image: url(:/img/pan.png);\n"
"border-radius: 35px;")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.comboBox_fan = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_fan.setGeometry(QtCore.QRect(120, 290, 71, 21))
        self.comboBox_fan.setStyleSheet("vborder-radius: 20px;\n"
"border: 1px black;\n"
"border-style: double;\n"
"background-color: #bbf0ee;\n"
"font: 15px Bahnschrift;\n"
"text-align: center;")
        self.comboBox_fan.setObjectName("comboBox_fan")
        self.comboBox_fan.addItem("")
        self.comboBox_fan.addItem("")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(30, 340, 71, 71))
        self.label_17.setStyleSheet("border-image: url(:/img/water.jpg);\n"
"border-radius: 35px;")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.comboBox_water = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_water.setGeometry(QtCore.QRect(30, 420, 71, 21))
        self.comboBox_water.setStyleSheet("border-radius: 20px;\n"
"border: 1px solid black; \n"
"background-color: #bbf0ee;\n"
"font: 15px Bahnschrift;\n"
"text-align: center;")
        self.comboBox_water.setObjectName("comboBox_water")
        self.comboBox_water.addItem("")
        self.comboBox_water.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(455, 100, 26, 2))
        self.label.setStyleSheet("border: 10px solid #313d3d;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(566, 100, 26, 2))
        self.label_4.setStyleSheet("border: 10px solid #313d3d;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(220, 140, 601, 351))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_temp = QtWidgets.QLabel(self.page_2)
        self.label_temp.setGeometry(QtCore.QRect(90, 75, 131, 51))
        self.label_temp.setStyleSheet("background-color: white;\n"
"border-radius: 70px;\n"
"font: 60px Bahnschrift;\n"
"font-weight: bold;\n"
"color: green;\n"
"")
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(30, 15, 251, 131))
        self.label_5.setStyleSheet("background-color: white;\n"
"border:1px solid black;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(130, 35, 52, 30))
        self.label_2.setStyleSheet("font: 25px Bahnschrift;")
        self.label_2.setObjectName("label_2")
        self.label_19 = QtWidgets.QLabel(self.page_2)
        self.label_19.setGeometry(QtCore.QRect(310, 15, 261, 131))
        self.label_19.setStyleSheet("background-color: white; border:1px solid black;")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(410, 35, 63, 30))
        self.label_15.setStyleSheet("font: 25px Bahnschrift;")
        self.label_15.setObjectName("label_15")
        self.label_humid = QtWidgets.QLabel(self.page_2)
        self.label_humid.setGeometry(QtCore.QRect(365, 75, 151, 51))
        self.label_humid.setStyleSheet("background-color: white;\n"
"border-radius: 70px;\n"
"font: 60px Bahnschrift;\n"
"font-weight: bold;\n"
"color: blue;\n"
"")
        self.label_humid.setAlignment(QtCore.Qt.AlignCenter)
        self.label_humid.setObjectName("label_humid")
        self.label_20 = QtWidgets.QLabel(self.page_2)
        self.label_20.setGeometry(QtCore.QRect(310, 170, 261, 131))
        self.label_20.setStyleSheet("background-color: white; border:1px solid black;")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(430, 190, 26, 30))
        self.label_9.setStyleSheet("font: 25px Bahnschrift;")
        self.label_9.setObjectName("label_9")
        self.label_ph = QtWidgets.QLabel(self.page_2)
        self.label_ph.setGeometry(QtCore.QRect(395, 225, 101, 54))
        self.label_ph.setStyleSheet("background-color: white;\n"
"border-radius: 70px;\n"
"font: 60px Bahnschrift;\n"
"font-weight: bold;\n"
"color: black;\n"
"")
        self.label_ph.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ph.setObjectName("label_ph")
        self.label_21 = QtWidgets.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(30, 170, 251, 131))
        self.label_21.setStyleSheet("background-color: white; border:1px solid black;")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(140, 190, 38, 30))
        self.label_7.setStyleSheet("font: 25px Bahnschrift;")
        self.label_7.setObjectName("label_7")
        self.label_co2 = QtWidgets.QLabel(self.page_2)
        self.label_co2.setGeometry(QtCore.QRect(110, 225, 101, 54))
        self.label_co2.setStyleSheet("background-color: white;\n"
"border-radius: 70px;\n"
"font: 60px Bahnschrift;\n"
"font-weight: bold;\n"
"color: red;\n"
"")
        self.label_co2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_co2.setObjectName("label_co2")
        self.label_5.raise_()
        self.label_temp.raise_()
        self.label_2.raise_()
        self.label_19.raise_()
        self.label_15.raise_()
        self.label_humid.raise_()
        self.label_20.raise_()
        self.label_9.raise_()
        self.label_ph.raise_()
        self.label_21.raise_()
        self.label_7.raise_()
        self.label_co2.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.graphicsView = PlotWidget(self.page)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 561, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(120, 340, 71, 71))
        self.label_18.setStyleSheet("border-image: url(:/img/CAMERA.JPG);\n"
"border-radius: 35px;\n"
"border-image: url(:/img/CAMERA.jpg);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.comboBox_picture = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_picture.setGeometry(QtCore.QRect(120, 420, 71, 21))
        self.comboBox_picture.setStyleSheet("vborder-radius: 20px;\n"
"border: 1px black;\n"
"border-style: double;\n"
"background-color: #bbf0ee;\n"
"font: 15px Bahnschrift;\n"
"text-align: center;")
        self.comboBox_picture.setObjectName("comboBox_picture")
        self.comboBox_picture.addItem("")
        self.comboBox_picture.addItem("")
        self.btn_main_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_main_off.setGeometry(QtCore.QRect(370, 86, 85, 31))
        self.btn_main_off.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255, 150);\n"
"color: black;\n"
"font: 15px;\n"
"font-weight: bold;\n"
"border-radius: 15px;\n"
"border: 1px solid black;}\n"
"QPushButton:hover{background-color: rgb(179, 179, 179, 150);\n"
"color: black;\n"
"font: 15px;\n"
"font-weight: bold;\n"
"border-radius: 15px;\n"
"border: 1px solid black;}\n"
"")
        self.btn_main_off.setObjectName("btn_main_off")
        self.btn_graph_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_graph_on.setGeometry(QtCore.QRect(481, 86, 85, 31))
        self.btn_graph_on.setStyleSheet("background-color: rgba(0, 0, 0, 170);\n"
"color: white;\n"
"font: 15px;\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"font-weight: bold;\n"
"")
        self.btn_graph_on.setObjectName("btn_graph_on")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(220, 0, 605, 131))
        self.label_25.setStyleSheet("background-color: white;\n"
"background-image: url(:/bg/sky.jpg);\n"
"border: 1px solid black;")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.btn_setting_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setting_2.setGeometry(QtCore.QRect(590, 86, 85, 31))
        self.btn_setting_2.setStyleSheet("background-color: rgba(0, 0, 0, 170);\n"
"color: white;\n"
"font: 15px;\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"font-weight: bold;\n"
"")
        self.btn_setting_2.setObjectName("btn_setting_2")
        self.btn_setting_2.raise_()
        self.btn_graph_on.raise_()
        self.btn_main_off.raise_()
        self.label_25.raise_()
        self.stackedWidget.raise_()
        self.label_3.raise_()
        self.label_26.raise_()
        self.label_date.raise_()
        self.label_time.raise_()
        self.label_29.raise_()
        self.label_31.raise_()
        self.label_33.raise_()
        self.label_27.raise_()
        self.label_30.raise_()
        self.comboBox_led.raise_()
        self.label_16.raise_()
        self.comboBox_fan.raise_()
        self.label_17.raise_()
        self.comboBox_water.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.btn_graph_off.raise_()
        self.btn_main_on.raise_()
        self.label_18.raise_()
        self.comboBox_picture.raise_()
        self.btn_setting.raise_()
        self.label_14.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_graph_off.clicked.connect(self.btn_graph_off.lower)
        self.btn_graph_off.clicked.connect(self.btn_main_on.lower)
        self.btn_graph_off.clicked.connect(self.btn_main_off.raise_)
        self.btn_graph_off.clicked.connect(self.btn_graph_on.raise_)
        self.btn_setting.clicked.connect(self.btn_setting.lower)
        self.btn_setting.clicked.connect(self.btn_setting_2.raise_)
        self.btn_setting.clicked.connect(self.btn_main_on.lower)
        self.btn_setting.clicked.connect(self.btn_main_off.raise_)
        self.btn_setting.clicked.connect(self.btn_graph_off.raise_)
        self.btn_setting.clicked.connect(self.btn_graph_on.lower)
        self.btn_graph_off.clicked.connect(self.btn_setting_2.lower)
        self.btn_graph_off.clicked.connect(self.btn_setting.raise_)
        self.btn_main_off.clicked.connect(self.btn_graph_on.lower)
        self.btn_main_off.clicked.connect(self.btn_setting_2.lower)
        self.btn_main_off.clicked.connect(self.btn_graph_off.raise_)
        self.btn_main_off.clicked.connect(self.btn_setting.raise_)
        self.btn_main_off.clicked.connect(self.btn_main_off.lower)
        self.btn_main_off.clicked.connect(self.btn_main_on.raise_)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_main_on.setText(_translate("MainWindow", "Main"))
        self.btn_graph_off.setText(_translate("MainWindow", "Graph"))
        self.btn_setting.setText(_translate("MainWindow", "Setting"))
        self.label_26.setText(_translate("MainWindow", "FARM"))
        self.label_time.setText(_translate("MainWindow", "00:00:00"))
        self.label_29.setText(_translate("MainWindow", "2019/07/30"))
        self.label_30.setText(_translate("MainWindow", "Control"))
        self.label_33.setText(_translate("MainWindow", "Timer"))
        self.label_27.setText(_translate("MainWindow", "SMART"))
        self.comboBox_led.setItemText(0, _translate("MainWindow", "Auto"))
        self.comboBox_led.setItemText(1, _translate("MainWindow", "Manual"))
        self.comboBox_fan.setItemText(0, _translate("MainWindow", "Auto"))
        self.comboBox_fan.setItemText(1, _translate("MainWindow", "Manual"))
        self.comboBox_water.setItemText(0, _translate("MainWindow", "Auto"))
        self.comboBox_water.setItemText(1, _translate("MainWindow", "Manual"))
        self.label_temp.setText(_translate("MainWindow", "00.0"))
        self.label_2.setText(_translate("MainWindow", "Temp"))
        self.label_15.setText(_translate("MainWindow", "Humid"))
        self.label_humid.setText(_translate("MainWindow", "00.0"))
        self.label_9.setText(_translate("MainWindow", "pH"))
        self.label_ph.setText(_translate("MainWindow", "00.0"))
        self.label_7.setText(_translate("MainWindow", "Co2"))
        self.label_co2.setText(_translate("MainWindow", "00.0"))
        self.comboBox_picture.setItemText(0, _translate("MainWindow", "Auto"))
        self.comboBox_picture.setItemText(1, _translate("MainWindow", "Manual"))
        self.btn_main_off.setText(_translate("MainWindow", "Main"))
        self.btn_graph_on.setText(_translate("MainWindow", "Graph"))
        self.btn_setting_2.setText(_translate("MainWindow", "Setting"))

from pyqtgraph import PlotWidget
from background import background

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

