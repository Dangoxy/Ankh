import ctypes
from moreInfoWindow import *
import sys


class moreInfoFunctions(QtWidgets.QMainWindow, Ui_moreInfoWindow):
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
myWindow = moreInfoFunctions()
myWindow.show()
app.exec_() """