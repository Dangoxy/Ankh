# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historyWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_historyWindow(object):
    def setupUi(self, historyWindow):
        historyWindow.setObjectName("historyWindow")
        historyWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(historyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 580, 530))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget{\n"
"background-color: rgba(255, 255, 255,25);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideNone)
        #self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        #self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setWordWrap(True)
        self.removeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.removeBtn.setGeometry(QtCore.QRect(380, 550, 210, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.removeBtn.setFont(font)
        self.removeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.removeBtn.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid rgb(105, 105, 157);\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"     background: rgba(170, 170, 255,95%)\n"
"    \n"
"    \n"
"    \n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(130, 130, 195);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(77, 77, 115);\n"
"    }")
        self.removeBtn.setFlat(False)
        self.removeBtn.setObjectName("removeBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.label.setStyleSheet("border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmall.png)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.listWidget.raise_()
        self.removeBtn.raise_()
        historyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(historyWindow)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(historyWindow)

    def retranslateUi(self, historyWindow):
        _translate = QtCore.QCoreApplication.translate
        historyWindow.setWindowTitle(_translate("historyWindow", "History"))
        self.removeBtn.setText(_translate("historyWindow", "Delete"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    historyWindow = QtWidgets.QMainWindow()
    ui = Ui_historyWindow()
    ui.setupUi(historyWindow)
    historyWindow.show()
    sys.exit(app.exec_())
