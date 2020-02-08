import sys
from PyQt4 import QtGui, QtCore
import os
#HOW TO INSTALL PyQt4
#sudo apt-get install qtcreator pyqt4-dev-tools
#sudo apt-get install python3-pyqt4
#sudo apt-get install qttools4-dev-tools

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("CENI")
        self.setWindowIcon(QtGui.QIcon('LogoCENI.png'))
        #palette = QtGui.QPalette()
        #palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QImage("index.jpeg")))
        #self.setPalette(palette)
        #self.centralwidget.setStyleSheet("background-image: url(index.jpeg); background-attachment: fixed")
        self.home()

    def home(self):
        btn1 = QtGui.QPushButton("upload",self)
        btn1.clicked.connect(self.upload_application)
        btn1.setGeometry(QtCore.QRect(100, 230, 100, 50))
        btn1.move(100,150)
        btn1.setIcon(QtGui.QIcon('Edit.png'))
        btn1.setMouseTracking(True)
        btn1.setStatusTip('Upload new documents')
        btn2 = QtGui.QPushButton("quit",self)
        btn2.clicked.connect(self.close_application)
        btn2.setGeometry(QtCore.QRect(100, 230, 100, 50))
	#resize(60,60)
        btn2.move(300,150)
        btn2.setIcon(QtGui.QIcon('Undo_icon.png'))
        btn2.setStatusTip('Leave the App')
        self.show()

    def upload_application(self):
        self.setWindowTitle("upload")
        os.system('python3 window.py')

    def close_application(self):
        #self.setWindowTitle("see you!!")
        sys.exit()
    #def show_statistic(self):



def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

main()
