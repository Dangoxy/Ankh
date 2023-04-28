import ctypes
from moreResultsWindow import *
import sys


class moreResultsFunctions(QtWidgets.QMainWindow, Ui_moreResultsWindow):
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
myWindow = moreResultsFunctions()
myWindow.show()
app.exec_() """