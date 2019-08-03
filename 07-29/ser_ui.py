# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ser_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 372)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 71, 76, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.ConnectButton = QtWidgets.QPushButton(Dialog)
        self.ConnectButton.setGeometry(QtCore.QRect(140, 72, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ConnectButton.setFont(font)
        self.ConnectButton.setObjectName("ConnectButton")
        self.clear_button = QtWidgets.QPushButton(Dialog)
        self.clear_button.setGeometry(QtCore.QRect(250, 72, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 110, 301, 181))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.Send_Edit = QtWidgets.QLineEdit(Dialog)
        self.Send_Edit.setGeometry(QtCore.QRect(30, 310, 221, 31))
        self.Send_Edit.setObjectName("Send_Edit")
        self.Send_Button = QtWidgets.QPushButton(Dialog)
        self.Send_Button.setGeometry(QtCore.QRect(260, 310, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Send_Button.setFont(font)
        self.Send_Button.setObjectName("Send_Button")

        self.retranslateUi(Dialog)
        self.clear_button.clicked.connect(self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Serial Test"))
        self.ConnectButton.setText(_translate("Dialog", "Connect"))
        self.clear_button.setText(_translate("Dialog", "clear"))
        self.label.setText(_translate("Dialog", "Serial Test Program"))
        self.Send_Button.setText(_translate("Dialog", "SEND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

