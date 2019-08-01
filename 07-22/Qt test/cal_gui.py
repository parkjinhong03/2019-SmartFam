# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(388, 164)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input1.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.input1.setObjectName("input1")
        self.input2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input2.setGeometry(QtCore.QRect(180, 40, 71, 16))
        self.input2.setObjectName("input2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 40, 51, 16))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(262, 38, 31, 16))
        self.label.setObjectName("label")
        self.result = QtWidgets.QLineEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(280, 40, 71, 16))
        self.result.setObjectName("result")
        self.Button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.Button_clear.setGeometry(QtCore.QRect(90, 90, 85, 23))
        self.Button_clear.setObjectName("Button_clear")
        self.Button_Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Calculate.setGeometry(QtCore.QRect(210, 90, 85, 23))
        self.Button_Calculate.setObjectName("Button_Calculate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 388, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Button_clear.clicked.connect(self.input1.clear)
        self.Button_clear.clicked.connect(self.input2.clear)
        self.Button_clear.clicked.connect(self.result.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "+"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-"))
        self.comboBox.setItemText(2, _translate("MainWindow", "*"))
        self.comboBox.setItemText(3, _translate("MainWindow", "/"))
        self.label.setText(_translate("MainWindow", "="))
        self.Button_clear.setText(_translate("MainWindow", "Clear"))
        self.Button_Calculate.setText(_translate("MainWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

