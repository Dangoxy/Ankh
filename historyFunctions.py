import ctypes
from historyWindow import *
import sys


class historyFunctions(QtWidgets.QMainWindow, Ui_historyWindow):
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
myWindow = historyFunctions()
myWindow.show()
app.exec_() """