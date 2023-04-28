import ctypes
from guideWindow import *
import sys


class guideFunctions(QtWidgets.QMainWindow, Ui_guideWindow):
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
myWindow = guideFunctions()
myWindow.show()
app.exec_() """