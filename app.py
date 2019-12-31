import sys
from PyQt4 import QtGui, QtCore
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
        #extractAction = QtGui.QAction("&GET IN SALMA!!",self)
        #extractAction.setShortcut("Ctrl+Q")
        #extractAction.setStatusTip('Leave the App')
        #extractAction.triggered.connect(self.close_application)
        #self.statusBar()
        #mainMenu = self.menuBar()
        #fileMenu = mainMenu.addMenu('&File')
        #fileMenu.addAction(extractAction)
        #fenetre_widget = QtGui.QWidget()
        #fenetre_widget.setStyleSheet("background-image: url(index.jpeg)")
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QImage("index.jpeg")))
        self.setPalette(palette)
        self.home()

    def home(self):
        btn1 = QtGui.QPushButton("upload",self)
        btn1.clicked.connect(self.upload_application)
        btn1.resize(80,80)
        btn1.move(10,50)
        btn1.setIcon(QtGui.QIcon('Edit.png'))
        btn1.setMouseTracking(True)
        btn1.setStatusTip('Upload new documents')
        btn2 = QtGui.QPushButton("show",self)
        #btn2.clicked.connect(self.show_statistic)
        btn2.resize(80,80)
        btn2.move(10,200)
        btn2.setIcon(QtGui.QIcon('refresh.png'))
        btn2.setStatusTip('Show the statistics')
        btn3 = QtGui.QPushButton("quit",self)
        btn3.clicked.connect(self.close_application)
        btn3.resize(80,80)
        btn3.move(10,350)
        btn3.setIcon(QtGui.QIcon('Undo_icon.png'))
        btn3.setStatusTip('Leave the App')
        self.show()

    def upload_application(self):
        self.setWindowTitle("upload")


    def close_application(self):
        #self.setWindowTitle("see you!!")
        sys.exit()
    #def show_statistic(self):



def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

main()
