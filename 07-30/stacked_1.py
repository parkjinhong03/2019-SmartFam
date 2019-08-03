# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stacked-1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(StackedWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 70, 571, 361))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 30, 400, 300))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(90, 40, 400, 300))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 40, 400, 300))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 40, 400, 300))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page_4)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 20, 501, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.push_1 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_1.sizePolicy().hasHeightForWidth())
        self.push_1.setSizePolicy(sizePolicy)
        self.push_1.setStyleSheet("QPushButton{\n"
"border-radius : 8px;\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 14pt \"Arial\";\n"
"}\n"
"QPushButton:checked {\n"
"border-radius : 8px;\n"
"background-color: rgb(170, 0, 0);\n"
"color: rgb(0, 0, 255);\n"
"font: 75 14pt \"Arial\";\n"
"}")
        self.push_1.setObjectName("push_1")
        self.horizontalLayout_2.addWidget(self.push_1)
        self.push_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_2.sizePolicy().hasHeightForWidth())
        self.push_2.setSizePolicy(sizePolicy)
        self.push_2.setStyleSheet("QPushButton{\n"
"border-radius : 8px;\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 14pt \"Arial\";\n"
"}\n"
"QPushButton:checked {\n"
"border-radius : 8px;\n"
"background-color: rgb(170, 0, 0);\n"
"color: rgb(0, 0, 255);\n"
"font: 75 14pt \"Arial\";\n"
"}")
        self.push_2.setObjectName("push_2")
        self.horizontalLayout_2.addWidget(self.push_2)
        self.push_3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_3.sizePolicy().hasHeightForWidth())
        self.push_3.setSizePolicy(sizePolicy)
        self.push_3.setStyleSheet("QPushButton{\n"
"border-radius : 8px;\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 14pt \"Arial\";\n"
"}\n"
"QPushButton:checked {\n"
"border-radius : 8px;\n"
"background-color: rgb(170, 0, 0);\n"
"color: rgb(0, 0, 255);\n"
"font: 75 14pt \"Arial\";\n"
"}")
        self.push_3.setObjectName("push_3")
        self.horizontalLayout_2.addWidget(self.push_3)
        self.push_4 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_4.sizePolicy().hasHeightForWidth())
        self.push_4.setSizePolicy(sizePolicy)
        self.push_4.setStyleSheet("QPushButton{\n"
"border-radius : 8px;\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 14pt \"Arial\";\n"
"}\n"
"QPushButton:checked {\n"
"border-radius : 8px;\n"
"background-color: rgb(170, 0, 0);\n"
"color: rgb(0, 0, 255);\n"
"font: 75 14pt \"Arial\";\n"
"}")
        self.push_4.setObjectName("push_4")
        self.horizontalLayout_2.addWidget(self.push_4)
        StackedWidget.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StackedWidget)
        self.statusbar.setObjectName("statusbar")
        StackedWidget.setStatusBar(self.statusbar)

        self.retranslateUi(StackedWidget)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.pushButton_2.setText(_translate("StackedWidget", "Page-1"))
        self.pushButton.setText(_translate("StackedWidget", "PAGE - 2"))
        self.pushButton_3.setText(_translate("StackedWidget", "PAGE - 3"))
        self.pushButton_4.setText(_translate("StackedWidget", "PAGE - 4"))
        self.push_1.setText(_translate("StackedWidget", "Push-1"))
        self.push_2.setText(_translate("StackedWidget", "Push-2"))
        self.push_3.setText(_translate("StackedWidget", "Push-3"))
        self.push_4.setText(_translate("StackedWidget", "Push-4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QMainWindow()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())

