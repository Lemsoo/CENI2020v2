
from PyQt4 import QtCore, QtGui
import os, sys
#from ceni.py import CENI

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
filePath = ""

class Window(QtGui.QMainWindow):

    global filePath

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("CENI")
        self.setWindowIcon(QtGui.QIcon('LogoCENI.png'))
        self.home()

    def home(self):
        
        lineEdit = QtGui.QLineEdit(self)
        lineEdit.setGeometry(QtCore.QRect(40, 100, 250, 40))
        lineEdit.setObjectName(_fromUtf8("lineEdit"))
        pushButton = QtGui.QPushButton("Go to files",self)
        #pushButton.resize(pushButton.sizeHint())
        pushButton.setGeometry(QtCore.QRect(40, 100, 100, 40))
        pushButton.move(300,100)
        pushButton.setObjectName(_fromUtf8("pushButton"))
        pushButton.setIcon(QtGui.QIcon('téléchargement.png'))
        pushButton.clicked.connect(self.Browse)
        Btn = QtGui.QPushButton("OK",self)
        Btn.setGeometry(QtCore.QRect(50, 50, 50, 50))
        Btn.setIcon(QtGui.QIcon('af4b043b9d.png'))
        Btn.move(200,200)
        Btn.clicked.connect(self.go)
        self.le = lineEdit
        self.show()

    def go(self):
        filePath = self.le.text()
        print(filePath)
        app = "ceni.py"
        cmd="python3 '%s' '%s'" % (app, filePath)
        os.system(cmd)
        msgBox = QtGui.QMessageBox()
        #msgBox.setIcon(Informative)
        msgBox.setText("Done with success !!")
        msgBox.setInformativeText("All the NNI are in the file nni.txt")
        msgBox.setWindowTitle("Success")
        #ret = msgBox.exec()
        msgBox.show()
        #msgBox.isVisible(True)

        #os.system('python3 ceni.py')
        #files = self.Browse.le.text()
        #print(files)

    
    def Browse(self):
	
        filePath = QtGui.QFileDialog.getOpenFileName(None, 
                                                       'Files',
                                                       '/root/home/Desktop',
                                                      '*.pdf')
        print('filePath :',filePath, '\n')
        
        fileHandle = open(filePath, 'r')
        self.le.setText(filePath)
        #filePath = .

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #CENI.pdf = self.Browse.filepath
    ui = Window()
    sys.exit(app.exec_())

