import ctypes
from addWindow import *
import sys


class addFunctions(QtWidgets.QMainWindow, Ui_addWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

        self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint, True)
        
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        self.setWindowIcon(QtGui.QIcon(
            ':icons\\icons\\ankh_icon.png'))
        
""" app = QtWidgets.QApplication(sys.argv)
myWindow = addFunctions()
myWindow.show()
app.exec_() """