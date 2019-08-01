from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_LED_Control(object):
    def setupUi(self, LED_Control):
        LED_Control.setObjectName("LED_Control")
        LED_Control.resize(447, 239)
        LED_Control.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.onButton = QtWidgets.QPushButton(LED_Control)
        self.onButton.setGeometry(QtCore.QRect(60, 70, 131, 81))
        self.onButton.setStyleSheet("background: rgb(170, 0, 0);\n" "color: rgb(255, 255, 255);\n" "font: 75 24pt \"Arial\";")
        self.onButton.setObjectName("onButton")
        self.offButton = QtWidgets.QPushButton(LED_Control)
        self.offButton.setGeometry(QtCore.QRect(250, 70, 131, 81))
        self.offButton.setStyleSheet("background: rgb(0, 0, 255);\n"  "font: 75 24pt \"Arial\";\n" "color: rgb(255, 255, 255);")
        self.offButton.setObjectName("offButton")
        self.retranslateUi(LED_Control)
        QtCore.QMetaObject.connectSlotsByName(LED_Control)

    def retranslateUi(self, LED_Control):
        _translate = QtCore.QCoreApplication.translate
        LED_Control.setWindowTitle(_translate("LED_Control", "LED_Control"))
        self.onButton.setText(_translate("LED_Control", "ON"))
        self.offButton.setText(_translate("LED_Control", "OFF"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LED_Control = QtWidgets.QDialog()
    ui = Ui_LED_Control()
    ui.setupUi(LED_Control)
    LED_Control.show()
    sys.exit(app.exec_())
