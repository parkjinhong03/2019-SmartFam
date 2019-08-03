from stacked_1 import *
import PyQt5
from functools import partial

class EventThread(PyQt5.QtCore.QThread):
 #   alertSignal = PyQt5.QtCore.pyqtSignal(str)

    def __init__(self, ui):
    #    super().__init__()    

        self.mainButton_list = [ui.push_1,ui.push_2,ui.push_3,ui.push_4]
        for i, mainButton in enumerate(self.mainButton_list):
            mainButton.clicked.connect(partial(ui.stackedWidget.setCurrentIndex,i))  
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_StackedWidget()
    ui.setupUi(MainWindow)
    eventThread = EventThread(ui)
    MainWindow.show()
    sys.exit(app.exec_())

