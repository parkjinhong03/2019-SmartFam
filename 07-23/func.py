from animal import *
import pygame
pygame.init()
pygame.mixer.init()



def signals(self):
    self.pushButton.clicked.connect(pig)
    self.pushButton_2.clicked.connect(cat)
    self.pushButton_3.clicked.connect(bird)
    self.pushButton_4.clicked.connect(wolf)

def pig():
    sounda = pygame.mixer.Sound('wav_animals/pig.wav')
    sounda.play()

def cat():
    sounda = pygame.mixer.Sound('wav_animals/cat.wav')
    sounda.play()

def bird():
    sounda = pygame.mixer.Sound('wav_animals/bird.wav')
    sounda.play()

def wolf():
    sounda = pygame.mixer.Sound('wav_animals/wolf.wav')
    sounda.play()



Ui_MainWindow.signals = signals


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())