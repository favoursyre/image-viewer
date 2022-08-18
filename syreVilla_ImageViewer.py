#I want create a main app with multiple windows embedded within ---> Embedded Image Viewer App

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMenuBar, QStatusBar, QPushButton, QFileDialog
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap 
import sys

class UI_ImageViewer(QMainWindow):
    #def __init__(self):
    def setupUi_Image(self, imgWindow):
        #super(UI_ImageViewer, self).__init__()

        #Section for loading the image viewer UI file that will be needed
        uic.loadUi("syreVilla_image.ui", self) 

        #Defining the various widgets for the image viewer window
        self.imageViewLabel = self.findChild(QLabel, "imageLabel")
        self.imageHideButton = self.findChild(QPushButton, "imageBackButton")
        self.imageUploadButton = self.findChild(QPushButton, "uploadButton")
        self.imageHomeButton = self.findChild(QPushButton, "imageHomeButton")

        #Button functionalities for main window
        self.imageHideButton.clicked.connect(self.hideMain)
        self.imageUploadButton.clicked.connect(self.imageUpload)

        self.show()

    def hideMain(self):
        self.hide()

    def imageUpload(self):
        fileName = QFileDialog.getOpenFileName(self, "Upload Image", "", "All Files (*);; PNG Files (*png);; JPG Files (*jpg)") #This opens and specifies the kind of file that I want
        self.pixmap = QPixmap(fileName[0]) #This gets the actual image file that was picked
        self.imageViewLabel.setPixmap(self.pixmap) #This uploads the image on the label


imageApp = QApplication(sys.argv)
thirdWindow = QtWidgets.QMainWindow()
UIWindowImage = UI_ImageViewer()
UIWindowImage.setupUi_Image(thirdWindow)

imageApp.exec_()
