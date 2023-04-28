from MainWindow import *
import sys
import mainFunctions
from PyQt5.QtCore import Qt
from dictionaryWindow import *
import ast
from PyQt5.QtCore import QTimer
from PyQt5 import sip
from PyQt5.QtWidgets import QFileDialog
import os
from mutualData import mutualData
import ctypes
from pathlib import Path
from dictionaryFunctions import dictionaryFunctions
from moreInfoFunctions import moreInfoFunctions
from settingsFunctions import settingsFunctions
from historyFunctions import historyFunctions
from moreResultsFunctions import moreResultsFunctions
from guideFunctions import guideFunctions
from addFunctions import addFunctions





#QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
#QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):

    #using the formater from the mainFunctions class, it formats the hieroglyphic symbols 
    # into categories from a to z making them dictionaries.
    
    a,b,c,d,e,f,g,h,i,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa = {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
    a,b,c,d,e,f,g,h,i,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa = mainFunctions.formater()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

        #settings some window flags, making it frameless, and transparent.

        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.CustomizeWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)


        #setting the window icon

        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        self.setWindowIcon(QtGui.QIcon(
            ':icons\\icons\\ankh_icon.png'))
        

        QtGui.QFontDatabase.addApplicationFont(":icons\\NotoSansEgyptianHieroglyphs-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont(":icons\\Transliteration.TTF")
        QtGui.QFontDatabase.addApplicationFont(":icons\\Bebas-Regular.ttf")
        #creating an object for all the other windows and function classes and mutual data.

        global dictionaryW
        dictionaryW = dictionaryFunctions()

        global md
        md = mutualData()

        global sw
        sw = settingsFunctions()

        global history
        history = historyFunctions()

        global mi
        mi = moreInfoFunctions()

        global mr
        mr = moreResultsFunctions()

        global guide
        guide = guideFunctions()

        global addW
        addW = addFunctions()

        #incase there isnt a saved settings file, it just makes the buttons with a white theme.

        if mutualData.btncolors == "":
            self.btnmakerall()
        if mutualData.defaultLanguage == "English":
            self.enRadioBtn.setChecked(True)

        #saving in the log file.

        mainFunctions.saveLog("Opened Ankh the application.")

        self.previoussaved = ""

        #making timers for date, saving settings, for the text edit update, and for the history saving.

        timerfordate = QTimer(self)
        timerfordate.timeout.connect(self.displayTime)
        timerfordate.start(1)
        
        self.timerforsave = QTimer(self)
        self.timerforsave.timeout.connect(self.rnorm)



        self.timerfortextedit = QTimer()
        self.timerfortextedit.timeout.connect(self.textResultChange)
        self.timerfortextedit.setSingleShot(True)

        self.timerforhistory = QTimer()
        self.timerforhistory.timeout.connect(self.historySaver)





        #reading the default settings using the function.

        self.defaultSettingsRead()
        self.guideChange()

        #adding functionality to the main gui.

        self.exitBtn.clicked.connect(self.exitWindow)
        self.minimizeBtn.clicked.connect(self.minimizeWindow)
        self.categoryComboBox.activated.connect(self.combochange)
        self.langComboBox.activated.connect(self.changeTextSize)
        self.langComboBox_2.activated.connect(self.changeTextSize)

        self.displayTime()

        self.settingsBtn.clicked.connect(self.opensettingswindow)

        self.en_arTextEdit.textChanged.connect(self.stti)

        self.dicBtn.clicked.connect(self.dicshowhide)
        self.historyBtn.clicked.connect(self.historyopen)
        self.guideBtn.clicked.connect(self.guideshowhide)
        self.moreresultsBtn.clicked.connect(self.mrshowhide)
        self.moreinfoBtn.clicked.connect(self.mishowhide)
        self.arRadioBtn.toggled.connect(self.changeLanguageWRadio)
        self.enRadioBtn.toggled.connect(self.changeLanguageWRadio)

        #adding functionality to the settings gui.

        sw.changeBtn.clicked.connect(self.changedictionaryinsettings)
        sw.darkmodeCheckbox.stateChanged.connect(self.darkmode)
        sw.boldtextCheckbox.stateChanged.connect(self.boldtext)
        sw.showdateCheckbox.stateChanged.connect(self.showdate)
        sw.showtimeCheckbox.stateChanged.connect(self.showtime)
        sw.saveBtn.clicked.connect(self.saveDefaultSettings)
        sw.cancelBtn.clicked.connect(sw.close)
        sw.comboBox.activated.connect(self.changeLanguageWCombobox)

        #adding functionality to history gui.
        
        history.removeBtn.clicked.connect(self.removefromhistory)

        self.exchangeBtn.clicked.connect(self.exchangefunction)

        #self.timerfortexteditNormal = Timer(1.0,self.textResultChange)
        #self.timerforhistoryNormal = Timer(5.0,self.historySaver)
   
    def guideChange(self):

        if mutualData.btncolors == "w" and mutualData.defaultLanguage == "English":
            
            guide.bgLabel.setStyleSheet("image: url(:/icons/ps files/allGuide/background.png);\n"
"min-width:800;\n"
"min-height: 558;\n"
"\n"
"margin: 0px 0px 0px 0px")
            guide.tabWidget.setStyleSheet("""QTabWidget::pane {
        border: 1px solid lightgray;
        bottom:-1px; 
        background: rgb(245, 245, 245);} 
        QTabBar::tab {
        background: rgb(230, 230, 230); 
        border: 1px solid lightgray; 
        padding: 8px;
        min-width:127;
        min-height: 16;
        max-height: 32;
            background-color:  rgb(170, 170, 255);
            color: rgb(51, 51, 51);} 
        QTabBar::tab:selected { 
        background: rgb(245, 245, 245); 
        margin-top: -1px; 
        background-color:  rgb(105, 105, 157);}""")
            guide.scrollAreaWidgetContents_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
    "")
            guide.label1_1.setStyleSheet("\n"
    "\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px;\n"
    "\n"
    "image:url(:/icons/ps files/allGuide/maingui.png);")
            guide.label1_2.setStyleSheet("image: url(:/icons/ps files/allGuide/mainguilabels.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_3.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui2.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_4.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui3.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_5.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui4.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label2.setStyleSheet("image: url(:/icons/ps files/allGuide/moreinfomoreresults.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label3_1.setStyleSheet("image: url(:/icons/ps files/allGuide/dictionary.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label3_2.setStyleSheet("image: url(:/icons/ps files/allGuide/dictionarylabels.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label4.setStyleSheet("image: url(:/icons/ps files/allGuide/settings.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label5.setStyleSheet("image: url(:/icons/ps files/allGuide/history.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.linkTextArea.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://drive.google.com/file/d/1k_FKNkO9uoJnRH7gdJpkjO0ekCcoAn-F/view?usp=sharing\"><span style=\" font-size:32pt; text-decoration: underline; color:#0000ff;\">https://drive.google.com/file/d/1k_FKNkO9uoJnRH7gdJpkjO0ekCcoAn-F/view?usp=sharing</span></a></p></body></html>")

        elif mutualData.btncolors == "d" and mutualData.defaultLanguage == "English":

            guide.bgLabel.setStyleSheet("image: url(:/icons/ps files/allGuide/backgroundd.png);\n"
"min-width:800;\n"
"min-height: 558;\n"
"\n"
"margin: 0px 0px 0px 0px")
            guide.tabWidget.setStyleSheet("""QTabWidget::pane {
        border: 1px solid lightgray;
        bottom:-1px; 
        background: rgb(245, 245, 245);} 
        QTabBar::tab {
        background: rgb(230, 230, 230); 
        border: 1px solid lightgray; 
        padding: 8px;
        min-width:127;
        min-height: 16;
        max-height: 32;
            background-color:  rgba(29, 55, 74,100%);
            color: rgb(255, 255, 255);} 
        QTabBar::tab:selected { 
        background: rgb(245, 245, 245); 
        margin-top: -1px; 
        background-color:  rgba(60, 85, 105,100%);}""")
            guide.scrollAreaWidgetContents_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
    "")
            guide.label1_1.setStyleSheet("\n"
    "\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px;\n"
    "\n"
    "image:url(:/icons/ps files/allGuide/mainguid.png);")
            guide.label1_2.setStyleSheet("image: url(:/icons/ps files/allGuide/mainguilabelsd.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_3.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui2d.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_4.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui3d.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_5.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui4d.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label2.setStyleSheet("image: url(:/icons/ps files/allGuide/moreinfomoreresultsd.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label3_1.setStyleSheet("image: url(:/icons/ps files/allGuide/dictionaryd.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label3_2.setStyleSheet("image: url(:/icons/ps files/allGuide/dictionarylabelsd.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label4.setStyleSheet("\n"
    "image: url(:/icons/ps files/allGuide/settingsd.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label5.setStyleSheet("image: url(:/icons/ps files/allGuide/historyd.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.linkTextArea.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://drive.google.com/file/d/1k_FKNkO9uoJnRH7gdJpkjO0ekCcoAn-F/view?usp=sharing\"><span style=\" font-size:32pt; text-decoration: underline; color:#0000ff;\">https://drive.google.com/file/d/1k_FKNkO9uoJnRH7gdJpkjO0ekCcoAn-F/view?usp=sharing</span></a></p></body></html>")

        elif mutualData.btncolors == "w" and mutualData.defaultLanguage == "Arabic":

            guide.bgLabel.setStyleSheet("image: url(:/icons/ps files/allGuide/backgroundar.png);\n"
"min-width:800;\n"
"min-height: 558;\n"
"\n"
"margin: 0px 0px 0px 0px")
            guide.tabWidget.setStyleSheet("""QTabWidget::pane {
        border: 1px solid lightgray;
        bottom:-1px; 
        background: rgb(245, 245, 245);} 
        QTabBar::tab {
        background: rgb(230, 230, 230); 
        border: 1px solid lightgray; 
        padding: 8px;
        min-width:127;
        min-height: 16;
        max-height: 32;
            background-color:  rgb(170, 170, 255);
            color: rgb(51, 51, 51);} 
        QTabBar::tab:selected { 
        background: rgb(245, 245, 245); 
        margin-top: -1px; 
        background-color:  rgb(105, 105, 157);}""")
            guide.scrollAreaWidgetContents_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
    "")
            guide.label1_1.setStyleSheet("\n"
    "\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px;\n"
    "\n"
    "image:url(:/icons/ps files/allGuide/mainguiar.png);")
            guide.label1_2.setStyleSheet("image: url(:/icons/ps files/allGuide/mainguilabelsar.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_3.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui2ar.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_4.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui3ar.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_5.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui4ar.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label2.setStyleSheet("image: url(:/icons/ps files/allGuide/moreinfomoreresultsar.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label3_1.setStyleSheet("image: url(:/icons/ps files/allGuide/dictionaryar.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label3_2.setStyleSheet("image: url(:/icons/ps files/allGuide/dictionarylabelsar.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label4.setStyleSheet("\n"
    "image: url(:/icons/ps files/allGuide/settingsar.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label5.setStyleSheet("image: url(:/icons/ps files/allGuide/historyar.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.linkTextArea.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://drive.google.com/file/d/1k_FKNkO9uoJnRH7gdJpkjO0ekCcoAn-F/view?usp=sharing\"><span style=\" font-size:32pt; text-decoration: underline; color:#0000ff;\">https://drive.google.com/file/d/1k_FKNkO9uoJnRH7gdJpkjO0ekCcoAn-F/view?usp=sharing</span></a></p></body></html>")

        elif mutualData.btncolors == "d" and mutualData.defaultLanguage == "Arabic":

            guide.bgLabel.setStyleSheet("image: url(:/icons/ps files/allGuide/backgroundard.png);\n"
"min-width:800;\n"
"min-height: 558;\n"
"\n"
"margin: 0px 0px 0px 0px")
            guide.tabWidget.setStyleSheet("""QTabWidget::pane {
        border: 1px solid lightgray;
        bottom:-1px; 
        background: rgb(245, 245, 245);} 
        QTabBar::tab {
        background: rgb(230, 230, 230); 
        border: 1px solid lightgray; 
        padding: 8px;
        min-width:127;
        min-height: 16;
        max-height: 32;
            background-color:  rgba(29, 55, 74,100%);
            color: rgb(255, 255, 255);} 
        QTabBar::tab:selected { 
        background: rgb(245, 245, 245); 
        margin-top: -1px; 
        background-color:  rgba(60, 85, 105,100%);}""")
            guide.scrollAreaWidgetContents_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
    "")
            guide.label1_1.setStyleSheet("\n"
    "\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px;\n"
    "\n"
    "image:url(:/icons/ps files/allGuide/mainguiardard.png);")
            guide.label1_2.setStyleSheet("image: url(:/icons/ps files/allGuide/mainguilabelsard.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_3.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui2ard.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_4.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui3ard.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label1_5.setStyleSheet("image: url(:/icons/ps files/allGuide/maingui4ard.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label2.setStyleSheet("image: url(:/icons/ps files/allGuide/moreinfomoreresultsard.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label3_1.setStyleSheet("image: url(:/icons/ps files/allGuide/dictionaryard.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 4px 0px")
            guide.label3_2.setStyleSheet("image: url(:/icons/ps files/allGuide/dictionarylabelsard.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label4.setStyleSheet("\n"
    "image: url(:/icons/ps files/allGuide/settingsard.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.label5.setStyleSheet("image: url(:/icons/ps files/allGuide/historyard.png);\n"
    "min-width:800;\n"
    "min-height: 558;\n"
    "\n"
    "margin: 0px 0px 0px 0px")
            guide.linkTextArea.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://drive.google.com/file/d/1k_FKNkO9uoJnRH7gdJpkjO0ekCcoAn-F/view?usp=sharing\"><span style=\" font-size:32pt; text-decoration: underline; color:#0000ff;\">https://drive.google.com/file/d/1k_FKNkO9uoJnRH7gdJpkjO0ekCcoAn-F/view?usp=sharing</span></a></p></body></html>")

    def exchangefunction(self):

        b1 = self.langComboBox.currentIndex()
        b2 = self.langComboBox_2.currentIndex()

        te1 = self.en_arTextEdit.toPlainText()
        te2 = self.hieroTextEdit_2.toPlainText()

        if (self.langComboBox_2.currentText() == " Hieroglyph") or (self.langComboBox_2.currentText() == " الهيروغليفية"):
            te2 = te2.replace("   " , " ")

        if (self.langComboBox_2.currentText() == " Gardners code") or (self.langComboBox_2.currentText() == " كود غاردينر"):
            te2 = te2.replace("  " , " ")

        if self.langComboBox.currentIndex() == 4 or self.langComboBox.currentIndex() == 5:
            b1 = b2

        if self.hieroTextEdit_2.toPlainText() == "":
            self.langComboBox.setCurrentIndex(b2)
            self.langComboBox_2.setCurrentIndex(b1)
        
        else:
            self.langComboBox.setCurrentIndex(b2)
            self.langComboBox_2.setCurrentIndex(b1)

            self.en_arTextEdit.setPlainText(te2)
            self.hieroTextEdit_2.setPlainText(te1)
        
        




        self.changeTextSize()



    def removefromhistory(self):

        #Function to remove data from the history gui, when clicked on the remove button, 
        # it returns the currently selected item and removes it. then it takes all the current data,
        # and writes it into the history file, reloads the history again and saves it to the log. 

        selectedItem = history.listWidget.selectedItems()
        if not selectedItem:
            return        
        for item in selectedItem:
            bruh =item.text() 

            history.listWidget.takeItem(history.listWidget.row(item))

        items = []
        sitems = ""
        for i in range(history.listWidget.count()):
            items.append(history.listWidget.item(i).text())
        
        for i in items:
            sitems += i

        with open("translationHistory.txt","w+",encoding='utf-8') as savefile:
            savefile.write(sitems)
        
        removed = bruh.replace("\n","")
        mainFunctions.saveLog("Removed the following from history: " + removed )

    def historyopen(self):

        #Show the history from the history filem and shows the history window.
        history.hide()
        self.historyshow()
        history.show()

    def historyshow(self):

        #Function that shows the history, first it reads the data saved in the history file
        # we first add the lines into the "temps" variable then we add them into the "thtemp"
        # variable again (to further format it) then in another loop we add the elements in one by one
        # in an "item" and making it editable. 

        temp = []
        temps = ""
        thtemp = []


        historyFileLocation = Path("translationHistory.txt")
        if historyFileLocation.is_file():
            history.listWidget.clear()
            with open("translationHistory.txt","r+",encoding='utf-8') as savefile:
                temp = savefile.readlines()
            
            if temp != "":
            
                for i in temp:
                    temps += i
                
                for i in temps.split("\n"):
                    thtemp.append(i)

                for i in thtemp:
                    if i != "":
                        if i != "\n":
                            i = i.replace("\n","")
                            
                            item = QtWidgets.QListWidgetItem((i + "\n"))
                            
                            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable )
                            history.listWidget.addItem(item)

    def historySaver(self):

        #It saves the history by taking the data from the text edits and current selected languages, 
        # it compares if the current data is similar to the previous one or not. If it is, it doesn't save it,
        # else, it saves it to the history file. 

        with open("translationHistory.txt","a+",encoding='utf-8') as savefile:

            time = QtCore.QTime.currentTime().toString("h:mm:ss AP")
            date = QtCore.QDate.currentDate().toString('dd/MM/yyyy')

            if self.en_arTextEdit.toPlainText() != "":

                savedText = ("[" + date + " " + time + "]=> " +
                            "Translated from" + self.langComboBox.currentText() + " to" + self.langComboBox_2.currentText()+ " => " +
                            self.en_arTextEdit.toPlainText() + " : " + self.hieroTextEdit_2.toPlainText() + "\n")
                
                similarity = mainFunctions.similar(savedText,mutualData.previoussaved)

                if similarity < 0.94:
                    mutualData.previoussaved = savedText
                    print(savedText + " MWF Line 648")
                    savefile.write(savedText)



    def stti(self):

        #timers for the history save and for the "main" translating function

        self.timerfortextedit.start(500)
        self.timerforhistory.start(5000)

    def changeLanguageWRadio(self):

        #If conditions to check the current checked radiobutton, changes the language using the function, 
        # and checks the combobox in the settings.

        if self.enRadioBtn.isChecked():
            self.makeAppEn()
            sw.comboBox.setCurrentIndex(0)
            mutualData.defaultLanguage = "English"
        elif self.arRadioBtn.isChecked():
            self.makeAppAr()
            sw.comboBox.setCurrentIndex(1)
            mutualData.defaultLanguage = "Arabic"

        self.guideChange()

    def changeLanguageWCombobox(self):

        #checks which language is selected from the settings combobox, and changes the language to the set one, 
        # and then checks whichever radio button with the selected language.

        if sw.comboBox.currentIndex() == 0:
            self.makeAppEn()
            self.enRadioBtn.setChecked(True)
            mutualData.defaultLanguage = "English"
        elif sw.comboBox.currentIndex() == 1:
            self.makeAppAr()
            self.arRadioBtn.setChecked(True)
            mutualData.defaultLanguage = "Arabic"
        self.guideChange()



    def makeAppAr(self):

        #The main language function, it sets the text of all elements in the gui to arabic.
        # (except for the dictionary window and add window, it uses the function in their class.)

        self.setWindowTitle(("Ankh"))
        self.enRadioBtn.setText(("الإنجليزية"))
        self.arRadioBtn.setText(("العربية"))
        self.guideBtn.setText(("دليل"))
        self.langComboBox.setItemText(0, (" الإنجليزية"))
        self.langComboBox.setItemText(1, (" الهيروغليفية"))
        self.langComboBox.setItemText(2, (" حرفي"))
        self.langComboBox.setItemText(3, (" كود غاردينر"))
        self.langComboBox.setItemText(4, (" اسماء (الإنجليزية)"))
        self.langComboBox.setItemText(5, (" اسماء (العربية)"))
        
        self.langComboBox_2.setItemText(0, (" الإنجليزية"))
        self.langComboBox_2.setItemText(1, (" الهيروغليفية"))
        self.langComboBox_2.setItemText(2, (" حرفي"))
        self.langComboBox_2.setItemText(3, (" كود غاردينر"))
        self.exitBtn.setText(("X"))
        self.minimizeBtn.setText(("--"))
        self.en_arTextEdit.setPlaceholderText((".اكتب النص هنا"))

        
        self.hieroTextEdit_2.setPlaceholderText((".يظهر المحتوى المترجم هنا"))

        
        self.categoryComboBox.setItemText(0, ("-. كل الرموز"))
        self.categoryComboBox.setItemText(1, ("A. الرجل ومهنه"))
        self.categoryComboBox.setItemText(2, ("B. المرأة ومهنها"))
        self.categoryComboBox.setItemText(3, ("C. مجسم الآلهة"))
        self.categoryComboBox.setItemText(4, ("D. اجزاء من جسم الانسان"))
        self.categoryComboBox.setItemText(5, ("E. الثدييات"))
        self.categoryComboBox.setItemText(6, ("F. أجزاء من الثدييات"))
        self.categoryComboBox.setItemText(7, ("G. طيور"))
        self.categoryComboBox.setItemText(8, ("H. اجزاء من الطيور"))
        self.categoryComboBox.setItemText(9, ("I. الحيوانات البرمائية والزواحف وما إلى ذلك"))
        self.categoryComboBox.setItemText(10, ("K. الأسماك وأجزاء من الأسماك"))
        self.categoryComboBox.setItemText(11, ("L. اللافقاريات والحيوانات الصغرى"))
        self.categoryComboBox.setItemText(12, ("M. الأشجار والنباتات"))
        self.categoryComboBox.setItemText(13, ("N. السماء والأرض والمياه"))
        self.categoryComboBox.setItemText(14, ("O. المباني ، أجزاء المباني ، إلخ"))
        self.categoryComboBox.setItemText(15, ("P. السفن وأجزاء السفن"))
        self.categoryComboBox.setItemText(16, ("Q. أثاث المنازل والجنائز"))
        self.categoryComboBox.setItemText(17, ("R. أثاث المعبد والشعارات المقدسة"))
        self.categoryComboBox.setItemText(18, ("S. التيجان ، اللباس ، العصي ، إلخ"))
        self.categoryComboBox.setItemText(19, ("T. حرب ، صيد ، مجزرة"))
        self.categoryComboBox.setItemText(20, ("U. الزراعة والحرف والمهن"))
        self.categoryComboBox.setItemText(21, ("V. حبل ، ألياف ، سلال ، أكياس ، إلخ"))
        self.categoryComboBox.setItemText(22, ("W. السفن الحجرية والخزفية"))
        self.categoryComboBox.setItemText(23, ("X. أرغفة وكعك"))
        self.categoryComboBox.setItemText(24, ("Y. كتابات ، ألعاب ، موسيقى"))
        self.categoryComboBox.setItemText(25, ("Z. العلامات مشتقة من الأشكال الهيراطيقية والهندسية"))
        self.categoryComboBox.setItemText(26, ("Aa. غير مصنف"))
        self.historyBtn.setText(("سجل"))
        self.dicBtn.setText(("قاموس"))
        self.settingsBtn.setText(("إعدادات"))
        self.categoryLabel.setText(("فئات: "))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.categoryLabel.setFont(font)
        self.dateLabel.setText(("22/22/2222"))
        self.timeLabel.setText(("00:00 AM"))
        self.moreinfoBtn.setText(("معلومات أكثر"))
        self.moreresultsBtn.setText(("نتائج أخرى"))
        self.categoryComboBox.setGeometry(QtCore.QRect(30, 300, 521, 31))
        self.categoryLabel.setGeometry(QtCore.QRect(551, 300, 81, 31))

        dictionaryW.setWindowTitle("القاموس")
        dictionaryW.addBtn.setText("اضف")
        dictionaryW.removeBtn.setText( "مسح")
        dictionaryW.saveBtn.setText("حفظ")
        dictionaryW.saveAsBtn.setText("حفظ باسم")
        dictionaryW.statusLabel.setText("حالة------------------------------------------------------------------------------------------------------")
        dictionaryW.changeDictionaryBtn.setText("تغيير القاموس")
        dictionaryW.currDictionairyLabel.setText("القاموس الحالي:")
        dictionaryW.currDictionaryLabelName.setGeometry(QtCore.QRect(480, 0, 360, 40))
        dictionaryW.currDictionairyLabel.setGeometry(QtCore.QRect(660, 0, 180, 40))
        dictionaryW.changeDictionaryBtn.setGeometry(QtCore.QRect(10, 5, 180, 30))

        sw.setWindowTitle("إعدادات")
        sw.l7.setText("أظهر الوقت:")
        sw.l3.setText("اللغة الرئيسية:")
        sw.l1.setText("القاموس الرئيسي:")
        sw.changeBtn.setText("تغير")
        sw.comboBox.setItemText(0, "الإنجليزية")
        sw.comboBox.setItemText(1, "العربية")
        sw.l6.setText("عرض التاريخ:")
        sw.l5.setText("نص عريض: ")
        sw.l4.setText("الوضع المظلم:")
        sw.saveBtn.setText("حفظ")
        sw.cancelBtn.setText("لغي")
        sw.statusLabel.setText("------------------------------------------------------")
        sw.l1.setGeometry(QtCore.QRect(155, 10, 201, 40))
        sw.changeBtn.setGeometry(QtCore.QRect(10, 14, 58, 32))
        sw.l2.setGeometry(QtCore.QRect(10, 70, 351, 40))
        sw.l3.setGeometry(QtCore.QRect(165, 130, 191, 40))
        sw.comboBox.setGeometry(QtCore.QRect(10, 134, 116, 32))
        sw.l4.setGeometry(QtCore.QRect(211, 190, 144, 40))
        sw.l5.setGeometry(QtCore.QRect(211, 250, 144, 40))
        sw.l6.setGeometry(QtCore.QRect(211, 310, 144, 40))
        sw.l7.setGeometry(QtCore.QRect(211, 370, 144, 40))
        sw.darkmodeCheckbox.setGeometry(QtCore.QRect(10, 194, 58, 32))
        sw.boldtextCheckbox.setGeometry(QtCore.QRect(10, 254, 58, 32))
        sw.showdateCheckbox.setGeometry(QtCore.QRect(10, 314, 58, 32))
        sw.showtimeCheckbox.setGeometry(QtCore.QRect(10, 374, 58, 32))
        
        history.removeBtn.setText("مسح")

        history.setWindowTitle("سجل")
        guide.setWindowTitle("دليل")

    def makeAppEn(self):

        #The main language function, it sets the text of all elements in the gui to english.
        # (except for the dictionary window and add window, it uses the function in their class.)

        self.setWindowTitle(("Ankh"))
        self.enRadioBtn.setText(("English"))
        self.arRadioBtn.setText(("Arabic"))
        self.guideBtn.setText(("Guide"))
        self.langComboBox.setItemText(0, (" English"))
        self.langComboBox.setItemText(1, (" Hieroglyph"))
        self.langComboBox.setItemText(2, (" Transliteration"))
        self.langComboBox.setItemText(3, (" Gardners code"))
        self.langComboBox.setItemText(4, (" Names (English)"))
        self.langComboBox.setItemText(5, (" Names (Arabic)"))
        self.langComboBox_2.setItemText(0, (" English"))
        self.langComboBox_2.setItemText(1, (" Hieroglyph"))
        self.langComboBox_2.setItemText(2, (" Transliteration"))
        self.langComboBox_2.setItemText(3, (" Gardners code"))
        self.exitBtn.setText(("X"))
        self.minimizeBtn.setText(("--"))
        self.en_arTextEdit.setPlaceholderText(("Type text here."))
        self.hieroTextEdit_2.setPlaceholderText(("Translated content shows here."))
        self.categoryComboBox.setItemText(0, ("-. All signs"))
        self.categoryComboBox.setItemText(1, ("A. Man and his Occupations"))
        self.categoryComboBox.setItemText(2, ("B. Woman and her Occupations"))
        self.categoryComboBox.setItemText(3, ("C. Anthropomorphic Deities"))
        self.categoryComboBox.setItemText(4, ("D. Parts of the Human Body"))
        self.categoryComboBox.setItemText(5, ("E. Mammals"))
        self.categoryComboBox.setItemText(6, ("F. Parts of Mammals"))
        self.categoryComboBox.setItemText(7, ("G. Birds"))
        self.categoryComboBox.setItemText(8, ("H. Parts of Birds"))
        self.categoryComboBox.setItemText(9, ("I. Amphibious Animals, Reptiles, etc."))
        self.categoryComboBox.setItemText(10, ("K. Fish and Parts of Fish"))
        self.categoryComboBox.setItemText(11, ("L. Invertebrates and Lesser Animals"))
        self.categoryComboBox.setItemText(12, ("M. Trees and Plants"))
        self.categoryComboBox.setItemText(13, ("N. Sky, Earth, Water"))
        self.categoryComboBox.setItemText(14, ("O. Buildings, Parts of Buildings, etc."))
        self.categoryComboBox.setItemText(15, ("P. Ships and Parts of Ships"))
        self.categoryComboBox.setItemText(16, ("Q. Domestics and Funerary Furniture"))
        self.categoryComboBox.setItemText(17, ("R. Temple Furniture and Sacred Emblems"))
        self.categoryComboBox.setItemText(18, ("S. Crowns, Dress, Staves, etc."))
        self.categoryComboBox.setItemText(19, ("T. Warfare, Hunting, Butchery"))
        self.categoryComboBox.setItemText(20, ("U. Agriculture, Crafts, and Professions"))
        self.categoryComboBox.setItemText(21, ("V. Rope, Fiber, Baskets, Bags, etc."))
        self.categoryComboBox.setItemText(22, ("W. Vessels of Stone and Earthenware"))
        self.categoryComboBox.setItemText(23, ("X. Loaves and Cakes"))
        self.categoryComboBox.setItemText(24, ("Y. Writings, Games, Music"))
        self.categoryComboBox.setItemText(25, ("Z. Strokes, Signs derived from Hieratic, Geometrical Figures"))
        self.categoryComboBox.setItemText(26, ("Aa. Unclassified"))
        self.historyBtn.setText(("History"))
        self.dicBtn.setText(("Dictionary"))
        self.settingsBtn.setText(("Settings"))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(12)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setText(("Category: "))
        self.dateLabel.setText(("22/22/2222"))
        self.timeLabel.setText(("00:00 AM"))
        self.moreinfoBtn.setText(("More info"))
        self.moreresultsBtn.setText(("More results"))
        self.categoryLabel.setGeometry(QtCore.QRect(30, 300, 81, 31))
        self.categoryComboBox.setGeometry(QtCore.QRect(120, 300, 521, 31))


        dictionaryW.setWindowTitle("Dictionary")
        dictionaryW.addBtn.setText("Add")
        dictionaryW.removeBtn.setText("Remove")
        dictionaryW.saveBtn.setText("Save")
        dictionaryW.saveAsBtn.setText("Save as")
        dictionaryW.statusLabel.setText("Status------------------------------------------------------------------------------------------------------")
        dictionaryW.changeDictionaryBtn.setText("Change dictionary")
        dictionaryW.currDictionairyLabel.setText("Current dictionary:")
        dictionaryW.currDictionairyLabel.setGeometry(QtCore.QRect(10, 0, 180, 40))
        dictionaryW.currDictionaryLabelName.setGeometry(QtCore.QRect(200, 0, 450, 40))
        dictionaryW.changeDictionaryBtn.setGeometry(QtCore.QRect(660, 5, 180, 30))



        sw.setWindowTitle("Settings")
        sw.l7.setText("Show time:")
        sw.l3.setText("Default language:")
        sw.l1.setText("Default dictionary:")
        sw.changeBtn.setText("Change")
        sw.comboBox.setItemText(0, "English")
        sw.comboBox.setItemText(1, "Arabic")
        sw.l6.setText("Show date:")
        sw.l5.setText("Bold text: ")
        sw.l4.setText("Dark mode: ")
        sw.saveBtn.setText("Save")
        sw.cancelBtn.setText("Cancel")
        sw.statusLabel.setText("------------------------------------------------------")

        sw.l7.setGeometry(QtCore.QRect(10, 370, 121, 40))
        sw.l3.setGeometry(QtCore.QRect(10, 130, 191, 40))
        sw.l1.setGeometry(QtCore.QRect(10, 10, 201, 40))
        sw.changeBtn.setGeometry(QtCore.QRect(300, 14, 58, 32))
        sw.showtimeCheckbox.setGeometry(QtCore.QRect(300, 374, 58, 32))
        sw.comboBox.setGeometry(QtCore.QRect(240, 134, 116, 32))
        sw.showdateCheckbox.setGeometry(QtCore.QRect(300, 314, 58, 32))
        sw.l6.setGeometry(QtCore.QRect(10, 310, 121, 40))
        sw.l5.setGeometry(QtCore.QRect(10, 250, 121, 40))
        sw.boldtextCheckbox.setGeometry(QtCore.QRect(300, 254, 58, 32))
        sw.l4.setGeometry(QtCore.QRect(10, 190, 121, 40))
        sw.darkmodeCheckbox.setGeometry(QtCore.QRect(300, 194, 58, 32))
        sw.l2.setGeometry(QtCore.QRect(10, 70, 351, 40))



        history.removeBtn.setText("Delete")
        history.setWindowTitle("History")
        guide.setWindowTitle("Guide")



    def saveDefaultSettings(self):

        #Saves default settings, by taking the data from the mutualData class, and then writes it
        # as a dictionary and saves it to the settings text file. and saves to the log. 

        if sw.darkmodeCheckbox.isChecked():
            mutualData.darkmodestat = True
        else:
            mutualData.darkmodestat = False
        
        if sw.boldtextCheckbox.isChecked():
            mutualData.boldtextstat = True
        else:
            mutualData.boldtextstat = False
        
        if sw.showdateCheckbox.isChecked():
            mutualData.showdatestat = True
        else:
            mutualData.showdatestat = False
        
        if sw.showtimeCheckbox.isChecked():
            mutualData.showtimestat = True
        else:
            mutualData.showtimestat = False
        
        if sw.comboBox.currentIndex() == 0:
            mutualData.defaultLanguage = "English"
        else:
            mutualData.defaultLanguage = "Arabic"

        mutualData.defaultdic = mutualData.directoryname

        mutualData.dictionaryForSettings["darkmode"] = mutualData.darkmodestat
        mutualData.dictionaryForSettings["boldtext"] = mutualData.boldtextstat
        mutualData.dictionaryForSettings["showdate"] = mutualData.showdatestat
        mutualData.dictionaryForSettings["showtime"] = mutualData.showtimestat
        mutualData.dictionaryForSettings["bgcolor"] = mutualData.btncolors
        mutualData.dictionaryForSettings["defaultdictionary"] = mutualData.defaultdic
        mutualData.dictionaryForSettings["defaultlanguage"] = mutualData.defaultLanguage
        mutualData.dictionaryForSettings["combo1"] = mutualData.combo1
        mutualData.dictionaryForSettings["combo2"] = mutualData.combo2

        with open("DefaultSettings.txt","w+") as self.settingsFile:
            temp = str(mutualData.dictionaryForSettings).replace(",",",\n")
            for line in temp.split("\n"):
                self.settingsFile.write(line + "\n")



        sw.statusLabel.setStyleSheet("color: rgb(0,255,0);")
        sw.statusLabel.setText("Saved successfully !")


        self.timerforsave.start(3000)

        mainFunctions.saveLog("Saved default settings.")
    
    def rnorm(self):

        #Returns the status label in the settings to the normal color.
        if mutualData.btncolors == "w":
            sw.statusLabel.setStyleSheet("color: rgb(105, 105, 157)")
            sw.statusLabel.setText("------------------------------------------------------")
        else:
            sw.statusLabel.setStyleSheet("color: rgb(255, 255, 255)")
            sw.statusLabel.setText("------------------------------------------------------")

    def defaultSettingsRead(self):

        #Reads the information from the text file, using literal_eval function, it detects that its a dictionary.
        # After that, it reads all the variables in the dictionary and sets the variables in mutual data to said variables,
        # Then calls the settings functions.  

        dd = ""
        if os.path.exists("DefaultSettings.txt"):
            with open("DefaultSettings.txt","r+") as self.settingsFile:
                if os.stat("DefaultSettings.txt").st_size != 0:
                    temp = (self.settingsFile.readlines())
                    for i in temp:
                        dd += i

                    
                    mutualData.dictionaryForSettings = ast.literal_eval(dd)

                    mutualData.btncolors = mutualData.dictionaryForSettings["bgcolor"]

                    sw.darkmodeCheckbox.setChecked(mutualData.dictionaryForSettings["darkmode"])
                    mutualData.darkmodestat = mutualData.dictionaryForSettings["darkmode"]
                    self.darkmode()
                    sw.boldtextCheckbox.setChecked(mutualData.dictionaryForSettings["boldtext"])
                    mutualData.boldtextstat = mutualData.dictionaryForSettings["boldtext"]
                    self.boldtext()
                    sw.showdateCheckbox.setChecked(mutualData.dictionaryForSettings["showdate"])
                    mutualData.showdatestat = mutualData.dictionaryForSettings["showdate"]
                    self.showdate()
                    sw.showtimeCheckbox.setChecked(mutualData.dictionaryForSettings["showtime"])
                    mutualData.showtimestat = mutualData.dictionaryForSettings["showtime"]
                    self.showtime()

                    if mutualData.dictionaryForSettings["defaultlanguage"] == "English":
                        sw.comboBox.setCurrentIndex(0)
                        self.enRadioBtn.setChecked(True)
                        self.makeAppEn()
                        mutualData.defaultLanguage = "English"
                    elif mutualData.dictionaryForSettings["defaultlanguage"] == "Arabic":
                        sw.comboBox.setCurrentIndex(1)
                        self.arRadioBtn.setChecked(True)
                        self.makeAppAr()
                        mutualData.defaultLanguage = "Arabic"

                    location = Path(mutualData.dictionaryForSettings["defaultdictionary"])
                    if location.is_file():
                        mutualData.directoryname = mutualData.dictionaryForSettings["defaultdictionary"]
                    else:
                        mutualData.directoryname = "dictionaries\\defaultDictionary.txt"




                    mutualData.combo1 = mutualData.dictionaryForSettings["combo1"]
                    mutualData.combo2 = mutualData.dictionaryForSettings["combo2"]

                    self.langComboBox.setCurrentIndex(mutualData.combo1)
                    self.langComboBox_2.setCurrentIndex(mutualData.combo2)

                    self.changedictionaryonstart()   
                    self.changeTextSize()
        else:
            self.darkmode()       
            
        

    def showtime(self):

        #Shows the element time.

        if sw.showtimeCheckbox.isChecked():
            self.timeLabel.show()
            print("show time checked MWF Line 1074")
        
        else:
            self.timeLabel.hide()
            print("show time unchecked MWF Line 1078")

    def showdate(self):

        #Shows the element date.

        if sw.showdateCheckbox.isChecked():
            self.dateLabel.show()
            print("show time checked Line 1086")
        
        else:
            self.dateLabel.hide()
            print("show time unchecked Line 1090")

    def boldtext(self):

        #Turns the textedits into bold text using the stylesheet. If its not checked, it returns it to normal.

        if sw.boldtextCheckbox.isChecked():
            
            if mutualData.btncolors == "w":
                self.en_arTextEdit.setStyleSheet("background-color:rgba(255, 255, 255,60%);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgb(105, 105, 157);\n"
                "font-weight: bold;")
                self.hieroTextEdit_2.setStyleSheet("background-color:rgba(255, 255, 255,60%);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgb(105, 105, 157);\n"
                "font-weight: bold;")
            
            if mutualData.btncolors =="d":
                self.en_arTextEdit.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgba(29, 55, 74,100%);\n"
                "font-weight: bold;")
                self.hieroTextEdit_2.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgba(29, 55, 74,100%);\n"
                "font-weight: bold;")
            print("bold text checked MWF Line 1106")

        elif not sw.boldtextCheckbox.isChecked():
            if mutualData.btncolors == "w":
                self.en_arTextEdit.setStyleSheet("background-color:rgba(255, 255, 255,60%);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgb(105, 105, 157);\n"
                "font-weight: normal;""")
                self.hieroTextEdit_2.setStyleSheet("background-color:rgba(255, 255, 255,60%);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgb(105, 105, 157);\n"
                "font-weight: normal;""")
            
            if mutualData.btncolors =="d":
                self.en_arTextEdit.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgba(29, 55, 74,100%);\n"
                "font-weight: normal;")
                self.hieroTextEdit_2.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgba(29, 55, 74,100%);\n"
                "font-weight: normal;")
            print("bold text unchecked MWF Line 1138")

    def darkmode(self):

        #If the darkmode check box is checked, it turns the GUI into dark mode using the stylesheets.
        # Else, it returns in to the normal theme. 

        if sw.darkmodeCheckbox.isChecked():
            #main gui changes
            self.dicBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(55, 55, 55,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")
            self.guideBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "border-bottom-right-radius:30px;\n"
            "background: rgba(55, 55, 55,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")
            self.historyBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(55, 55, 55,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")
            self.moreinfoBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(55, 55, 55,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")
            self.settingsBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(55, 55, 55,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")
            self.moreinfoBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(55, 55, 55,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")
            self.moreresultsBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(55, 55, 55,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")            
            self.mainLabel.setStyleSheet("background-color:rgb(179, 179, 213);\n"
                "border-top-left-radius:75px;\n"
                "border-bottom-left-radius:75px;\n"
                "border-bottom-right-radius:75px;\n"
                "image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13bedark.png);\n")           
            print("dark mode checked MWF Line 1223")
            self.langComboBox.setStyleSheet("""QComboBox{
                background-color: rgba(55, 55, 55,95);
                border: 2px solid rgb(10, 40, 55);
                border-radius: 6px;
                border-top-left-radius:25px;
                border-bottom-left-radius:5px;
                color: rgb(200, 200, 200);}
            QComboBox::drop-down:button{
                border-radius:5px;
                background-color: rgb(50, 50, 50);}
            QComboBox::down-arrow{
                image: url(:/icons/icons/arrowdowndark.png);
                width: 12px;
                height: 12px;}
            QListView {
                background: rgba(55, 55, 55,95);
                border: 2px solid rgb(10, 40, 55);
                color: rgb(200, 200, 200);}""")
            self.langComboBox_2.setStyleSheet("""QComboBox{
                background-color: rgba(55, 55, 55,95);
                border: 2px solid rgb(10, 40, 55);
                border-radius:5px;
                color: rgb(200, 200, 200);}
            QComboBox::drop-down:button{
                border-radius:5px;
                background-color: rgb(50, 50, 50);}
            QComboBox::down-arrow{
                image: url(:/icons/icons/arrowdowndark.png);
                width: 12px;
                height: 12px;}
            QListView {
                background: rgba(55, 55, 55,95);
                border: 2px solid rgb(10, 40, 55);
                color: rgb(200, 200, 200);}""")            
            self.categoryComboBox.setStyleSheet("""QComboBox{
                background-color: rgba(55, 55, 55,95);
                border: 2px solid rgb(10, 40, 55);
                border-radius:5px;
                color: rgb(200, 200, 200);}
            QComboBox::drop-down:button{
                border-radius:5px;
                background-color: rgb(50, 50, 50);}
            QComboBox::down-arrow{
                image: url(:/icons/icons/arrowdowndark.png);
                width: 12px;
                height: 12px;}
            QListView {
                background: rgba(55, 55, 55,95);
                border: 2px solid rgb(10, 40, 55);
                color: rgb(200, 200, 200);}""")
            self.categoryLabel.setStyleSheet(("color: rgb(200, 200, 200);"))
            self.hieroTextEdit_2.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgba(29, 55, 74,100%);\n")         
            self.en_arTextEdit.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgba(29, 55, 74,100%);\n")
            self.scrollArea.setStyleSheet("""QScrollArea{
                background-color:rgba(255, 255, 255,50%);
                border: 2px;
                border-style: solid;
                border-color: rgb(29, 55, 74);}
                QWidget{
                background-color: rgba(0,0,0,10%);}
                QScrollBar:vertical {
			background-color: none;
            border: 0px solid #999999;
            background-color: rgb(34, 35, 52);
            width:16px;    
            margin: 16px 1px 16px 0px;
        }
        QScrollBar::handle:vertical {         
            min-height: 24px;
            border: 0px solid red;
            background-color:rgb(29, 55, 74);
        }
        QScrollBar::add-line:vertical { 
			      
			image: url(:/icons/icons/arrowdowndark.png);
            height: 16px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
			margin: 0px 1px 0px 1px;
        }
        QScrollBar::sub-line:vertical {
			
			image: url(:/icons/icons/arrowupdark.png);
            height: 16 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
			margin: 0px 1px 0px 1px;
        }

	QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: rgb(255, 255, 255);
	;
}""")
            self.exchangeBtn.setStyleSheet("""QPushButton {border-image: url(:/icons/icons/exchangedark.png);}
            QPushButton:pressed {
    border-style: inset;
    background: rgba(0, 0, 0,10%);
        border-radius: 10px;
    }""")
            mutualData.btncolors = "d"
            self.categoryComboBox.setCurrentIndex(0)
            self.widdel()
            self.btnmakerall()
            self.guideChange()



            sw.boldtextCheckbox.setStyleSheet("""QCheckBox::indicator:unchecked:hover {
	border-image:url(:/icons/icons/Toggle off2darkh.png);
	width: 58px;
	height: 32px;} 
 QCheckBox::indicator:checked:hover {
	border-image:url(:/icons/icons/Toggle on2darkh.png);
	width: 58px;
	height: 32px;} 
QCheckBox::indicator:unchecked {
	border-image: url(:/icons/icons/Toggle off2dark.png);
	width: 58px;
	height: 32px;}
    QCheckBox::indicator:checked {
	border-image: url(:/icons/icons/Toggle on2dark.png);
	width:58px;
	height:32px;}""")
            sw.darkmodeCheckbox.setStyleSheet("""QCheckBox::indicator:unchecked:hover {
	border-image:url(:/icons/icons/Toggle off2darkh.png);
	width: 58px;
	height: 32px;} 
 QCheckBox::indicator:checked:hover {
	border-image:url(:/icons/icons/Toggle on2darkh.png);
	width: 58px;
	height: 32px;} 
QCheckBox::indicator:unchecked {
	border-image: url(:/icons/icons/Toggle off2dark.png);
	width: 58px;
	height: 32px;}
    QCheckBox::indicator:checked {
	border-image: url(:/icons/icons/Toggle on2dark.png);
	width:58px;
	height:32px;}""")
            sw.showdateCheckbox.setStyleSheet("""QCheckBox::indicator:unchecked:hover {
	border-image:url(:/icons/icons/Toggle off2darkh.png);
	width: 58px;
	height: 32px;} 
 QCheckBox::indicator:checked:hover {
	border-image:url(:/icons/icons/Toggle on2darkh.png);
	width: 58px;
	height: 32px;} 
QCheckBox::indicator:unchecked {
	border-image: url(:/icons/icons/Toggle off2dark.png);
	width: 58px;
	height: 32px;}
    QCheckBox::indicator:checked {
	border-image: url(:/icons/icons/Toggle on2dark.png);
	width:58px;
	height:32px;}""")
            sw.showtimeCheckbox.setStyleSheet("""QCheckBox::indicator:unchecked:hover {
	border-image:url(:/icons/icons/Toggle off2darkh.png);
	width: 58px;
	height: 32px;} 
 QCheckBox::indicator:checked:hover {
	border-image:url(:/icons/icons/Toggle on2darkh.png);
	width: 58px;
	height: 32px;} 
QCheckBox::indicator:unchecked {
	border-image: url(:/icons/icons/Toggle off2dark.png);
	width: 58px;
	height: 32px;}
    QCheckBox::indicator:checked {
	border-image: url(:/icons/icons/Toggle on2dark.png);
	width:58px;
	height:32px;}""")
            sw.mainLabel.setStyleSheet("border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmalldark.png);")
            sw.saveBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(75, 75, 75,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")            
            sw.cancelBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(75, 75, 75,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")            
            sw.changeBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(75, 75, 75,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n") 
            sw.comboBox.setStyleSheet("""QComboBox{
                background-color: rgba(55, 55, 55,95);
                border: 2px solid rgb(10, 40, 55);
                border-radius:5px;
                color: rgb(200, 200, 200);}
            QComboBox::drop-down:button{
                border-radius:4px;
                background-color: rgb(50, 50, 50);}
            QComboBox::down-arrow{
                image: url(:/icons/icons/arrowdowndark.png);
                width: 12px;
                height: 12px;}
            QListView {
                background: rgba(55, 55, 55,95);
                border: 2px solid rgb(10, 40, 55);
                color: rgb(200, 200, 200);}""")            
            sw.statusLabel.setStyleSheet("color: rgb(255,255,255);")



            dictionaryW.addBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(75, 75, 75,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")                        
            dictionaryW.saveBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(75, 75, 75,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")                        
            dictionaryW.removeBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(75, 75, 75,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")                        
            dictionaryW.saveAsBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(75, 75, 75,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")                        
            dictionaryW.changeDictionaryBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(75, 75, 75,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")                        
            dictionaryW.mainBackgroundLabel.setStyleSheet("border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmalldark.png);")
            dictionaryW.statusLabel.setStyleSheet("color: rgb(200, 200, 200);")
            dictionaryW.currDictionaryLabelName.setStyleSheet("color: rgb(200, 200, 200);")
            dictionaryW.currDictionairyLabel.setStyleSheet("color: rgb(200, 200, 200);")
            dictionaryW.listWidget.setStyleSheet("QListWidget{\n"
"background-color: rgba(0, 0, 0,75%);\n"
"color: rgb(200, 200, 200);}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")



            history.removeBtn.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(75, 75, 75,95%);\n"
	        "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n")                                    
            history.label.setStyleSheet("border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmalldark.png);")
            history.listWidget.setStyleSheet("QListWidget{\n"
"background-color: rgba(0, 0, 0,75%);\n"
"color: rgb(200, 200, 200);}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")



            mi.mainLabel.setStyleSheet("border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmalldark.png);")
            mi.textEdit.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
                "color: rgb(200, 200, 200);\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgba(29, 55, 74,100%);\n")         
            mr.mainLabel.setStyleSheet("border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmalldark.png);")
            mr.textedit.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
                "color: rgb(200, 200, 200);\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgba(29, 55, 74,100%);\n")         

        else:
            #main gui reverts
            self.dicBtn.setStyleSheet("QPushButton {\n"
            "color: #333;\n"
            "border: 2px solid rgb(105, 105, 157);\n"
            "border-radius: 10px;\n"
            "\n"
            "background: rgba(170, 170, 255,95%)\n}"
            "QPushButton:hover {\n"
            "background: rgb(130, 130, 195);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(77, 77, 115);}\n")
            self.guideBtn.setStyleSheet("QPushButton {\n"
            "color: #333;\n"
            "border: 2px solid rgb(105, 105, 157);\n"
            "border-radius: 10px;\n"
            "border-bottom-right-radius:30px;\n"
            "\n"
            "background: rgba(170, 170, 255,95%)\n}"
            "QPushButton:hover {\n"
            "background: rgb(130, 130, 195);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(77, 77, 115);}\n")
            self.historyBtn.setStyleSheet("QPushButton {\n"
            "color: #333;\n"
            "border: 2px solid rgb(105, 105, 157);\n"
            "border-radius: 10px;\n"
            "background: rgba(170, 170, 255,95%)\n}"
            "QPushButton:hover {\n"
            "background: rgb(130, 130, 195);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(77, 77, 115);}\n")
            self.moreinfoBtn.setStyleSheet("QPushButton {\n"
            "color: #333;\n"
            "border: 2px solid rgb(105, 105, 157);\n"
            "border-radius: 10px;\n"
            "background: rgba(170, 170, 255,95%)\n}"
            "QPushButton:hover {\n"
            "background: rgb(130, 130, 195);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(77, 77, 115);}\n")
            self.settingsBtn.setStyleSheet("QPushButton {\n"
            "color: #333;\n"
            "border: 2px solid rgb(105, 105, 157);\n"
            "border-radius: 10px;\n"
            "background: rgba(170, 170, 255,95%)\n}"
            "QPushButton:hover {\n"
            "background: rgb(130, 130, 195);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(77, 77, 115);}\n")
            self.moreinfoBtn.setStyleSheet("QPushButton {\n"
            "color: #333;\n"
            "border: 2px solid rgb(105, 105, 157);\n"
            "border-radius: 10px;\n"
            "background: rgba(170, 170, 255,95%)\n}"
            "QPushButton:hover {\n"
            "background: rgb(130, 130, 195);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(77, 77, 115);}\n")
            self.moreresultsBtn.setStyleSheet("QPushButton {\n"
            "color: #333;\n"
            "border: 2px solid rgb(105, 105, 157);\n"
            "border-radius: 10px;\n"
            "background: rgba(170, 170, 255,95%)\n}"
            "QPushButton:hover {\n"
            "background: rgb(130, 130, 195);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(77, 77, 115);}\n")            
            self.mainLabel.setStyleSheet("background-color:rgb(179, 179, 213);\n"
                "border-top-left-radius:75px;\n"
                "border-bottom-left-radius:75px;\n"
                "border-bottom-right-radius:75px;\n"
                "image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13be.png);\n")
            print("dark mode unchecked MWF Line 1632")           
            self.langComboBox.setStyleSheet("""QComboBox{
                background-color: rgb(170, 170, 255);
                border: 2px solid rgb(105, 105, 157);
                border-radius: 6px;
                border-top-left-radius:25px;
                border-bottom-left-radius:5px;}
                QListView {
                background: rgb(170, 170, 255);
                border: 1px solid gray;}
                QComboBox::drop-down:button{
                border-radius:2px;
                width: 18px;
                height: 37px;
                background-color: rgb(117, 117, 175);}
                QComboBox::down-arrow{
                image: url(:/icons/icons/arrowdown.png);
                width: 12px;
                height: 12px;}""")            
            self.langComboBox_2.setStyleSheet("""QComboBox{
                background-color: rgb(170, 170, 255);
                border: 2px solid rgb(105, 105, 157);
                border-radius: 6px;
                border-bottom-left-radius:5px;}
                QListView {
                background: rgb(170, 170, 255);
                border: 1px solid gray;}
                QComboBox::drop-down:button{
                border-radius:2px;
                width: 18px;
                height: 37px;
                background-color: rgb(117, 117, 175);}
                QComboBox::down-arrow{
                image: url(:/icons/icons/arrowdown.png);
                width: 12px;
                height: 12px;}""")
            self.categoryComboBox.setStyleSheet("""QComboBox{
                background-color: rgb(170, 170, 255);
                border: 2px solid rgb(105, 105, 157);
                border-radius:8px;}
                QListView {
                background: rgb(170, 170, 255);
                border: 1px solid gray;}
                QComboBox::drop-down:button{
                border-radius:5px;
                width: 18px;
                height: 27px;
                background-color: rgb(117, 117, 175);}
                QComboBox::down-arrow{
                image: url(:/icons/icons/arrowdown.png);
                width: 12px;
                height: 12px;}""")
            self.categoryLabel.setStyleSheet(("color: rgb(0, 0, 0);"))
            self.hieroTextEdit_2.setStyleSheet("background-color:rgba(255, 255, 255,60%);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgb(105, 105, 157);\n""")
            self.en_arTextEdit.setStyleSheet("background-color:rgba(255, 255, 255,60%);\n"
                "border-radius:10px;\n"
                "border: 2px;\n"
                "border-style: solid;\n"
                "border-color: rgb(105, 105, 157);\n""")
            self.scrollArea.setStyleSheet("""QScrollArea{
                background-color:rgba(255, 255, 255,100);
                border: 2px;
                border-style: solid;
                border-color: rgb(105, 105, 157);}
                QWidget{
                background-color: rgba(255,255,255,60%);}
                QScrollBar:vertical {
			background-color: none;
            border: 0px solid #999999;
            background-color: rgb(34, 35, 52);
            width:16px;    
            margin: 16px 1px 16px 0px;
        }
        QScrollBar::handle:vertical {         
            min-height: 24px;
            border: 0px solid red;
            background-color:rgb(105, 105, 157);
        }
        QScrollBar::add-line:vertical { 
			      
			image: url(:/icons/icons/arrowdown.png);
            height: 16px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
			margin: 0px 1px 0px 1px;
        }
        QScrollBar::sub-line:vertical {
			
			image: url(:/icons/icons/arrowup.png);
            height: 16 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
			margin: 0px 1px 0px 1px;
        }

	QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: rgb(255, 255, 255);
	;
}""")
            self.exchangeBtn.setStyleSheet("""QPushButton {border-image: url(:/icons/icons/exchange.png);}
            QPushButton:pressed {
    border-style: inset;
    background: rgba(255, 255, 255,10%);
    border-radius: 10px;
    }""")
            mutualData.btncolors = "w"
            self.categoryComboBox.setCurrentIndex(0)
            self.widdel()
            self.btnmakerall()
            self.guideChange()

            

            sw.mainLabel.setStyleSheet("\n"
"border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmall.png);")
            sw.changeBtn.setStyleSheet("QPushButton {\n"
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
            sw.showtimeCheckbox.setStyleSheet(" QCheckBox::indicator:unchecked:hover {\n"
            "    border-image:url(:/icons/icons/Toggle off2h.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "} \n"
            " QCheckBox::indicator:checked:hover {\n"
            "    border-image:url(:/icons/icons/Toggle on2h.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "} \n"
            "QCheckBox::indicator:unchecked {\n"
            "    border-image: url(:/icons/icons/Toggle off2.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "    \n"
            "    }\n"
            "    QCheckBox::indicator:checked {\n"
            "    \n"
            "    border-image: url(:/icons/icons/Toggle on2.png);\n"
            "    width:58px;\n"
            "    height:32px;\n"
            "    }")
            sw.comboBox.setStyleSheet("""QComboBox{
                background-color: rgb(170, 170, 255);
                border: 2px solid rgb(105, 105, 157);
                border-radius:5px;
                background: rgb(170, 170, 255);}
            QComboBox::drop-down:button{
                border-radius:5px;
                background-color: rgb(117, 117, 175);}
            QComboBox::down-arrow{
                image: url(:/icons/icons/arrowdown.png);
                width: 12px;
                height: 12px;}
            QListView {
                background: rgb(170, 170, 255);
                border: 4px solid gray;;
                color: rgb(200, 200, 200);}""")
            
            sw.showdateCheckbox.setStyleSheet(" QCheckBox::indicator:unchecked:hover {\n"
            "    border-image:url(:/icons/icons/Toggle off2h.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "} \n"
            " QCheckBox::indicator:checked:hover {\n"
            "    border-image:url(:/icons/icons/Toggle on2h.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "} \n"
            "QCheckBox::indicator:unchecked {\n"
            "    border-image: url(:/icons/icons/Toggle off2.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "    \n"
            "    }\n"
            "    QCheckBox::indicator:checked {\n"
            "    \n"
            "    border-image: url(:/icons/icons/Toggle on2.png);\n"
            "    width:58px;\n"
            "    height:32px;\n"
            "    }")
            sw.boldtextCheckbox.setStyleSheet(" QCheckBox::indicator:unchecked:hover {\n"
            "    border-image:url(:/icons/icons/Toggle off2h.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "} \n"
            " QCheckBox::indicator:checked:hover {\n"
            "    border-image:url(:/icons/icons/Toggle on2h.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "} \n"
            "QCheckBox::indicator:unchecked {\n"
            "    border-image: url(:/icons/icons/Toggle off2.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "    \n"
            "    }\n"
            "    QCheckBox::indicator:checked {\n"
            "    \n"
            "    border-image: url(:/icons/icons/Toggle on2.png);\n"
            "    width:58px;\n"
            "    height:32px;\n"
            "    }")
            sw.darkmodeCheckbox.setStyleSheet(" QCheckBox::indicator:unchecked:hover {\n"
            "    border-image:url(:/icons/icons/Toggle off2h.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "} \n"
            " QCheckBox::indicator:checked:hover {\n"
            "    border-image:url(:/icons/icons/Toggle on2h.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "} \n"
            "QCheckBox::indicator:unchecked {\n"
            "    border-image: url(:/icons/icons/Toggle off2.png);\n"
            "    width: 58px;\n"
            "    height: 32px;\n"
            "    \n"
            "    }\n"
            "    QCheckBox::indicator:checked {\n"
            "    \n"
            "    border-image: url(:/icons/icons/Toggle on2.png);\n"
            "    width:58px;\n"
            "    height:32px;\n"
            "    }")
            sw.saveBtn.setStyleSheet("QPushButton {\n"
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
            sw.cancelBtn.setStyleSheet("QPushButton {\n"
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
            sw.statusLabel.setStyleSheet("color: rgb(105, 105, 157);")



            dictionaryW.addBtn.setStyleSheet("QPushButton {\n"
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
            dictionaryW.saveBtn.setStyleSheet("QPushButton {\n"
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
            dictionaryW.removeBtn.setStyleSheet("QPushButton {\n"
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
            dictionaryW.saveAsBtn.setStyleSheet("QPushButton {\n"
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
            dictionaryW.changeDictionaryBtn.setStyleSheet("QPushButton {\n"
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
            dictionaryW.mainBackgroundLabel.setStyleSheet("\n"
"border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmall.png);")     
            dictionaryW.statusLabel.setStyleSheet("color: rgb(105, 105, 157);")
            dictionaryW.currDictionaryLabelName.setStyleSheet("color: rgb(37, 37, 37);\n"
"")
            dictionaryW.currDictionairyLabel.setStyleSheet("color: #333;")
            dictionaryW.listWidget.setStyleSheet("QListWidget{\n"
"background-color: rgba(255, 255, 255,25);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")



            history.removeBtn.setStyleSheet("QPushButton {\n"
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
            history.label.setStyleSheet("border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmall.png)")        
            history.listWidget.setStyleSheet("QListWidget{\n"
"background-color: rgba(255, 255, 255,25);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")            
            
            
            
            mi.mainLabel.setStyleSheet("\n"
"border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmall.png);")       
            mi.textEdit.setStyleSheet("background-color:rgba(255, 255, 255,25%);\n"
"border: 2px;\n"
"border-style: solid;\n"
"border-color: rgb(105, 105, 157);\n"
"")
            mr.mainLabel.setStyleSheet("\n"
"border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmall.png);")       
            mr.textedit.setStyleSheet("background-color:rgba(255, 255, 255,25%);\n"
"border: 2px;\n"
"border-style: solid;\n"
"border-color: rgb(105, 105, 157);\n"
"")

        

            



    def opensettingswindow(self):

        #Sets the dictionary in the settings' label to the current dictionary name, and then opens the window.
        sw.hide()
        sw.l2.setText(md.filename)

        sw.show()        

    def changedictionaryinsettings(self):

        #Using the getOpenFileName function, we get the dictionary name, then if it isnt canceled or unavailable,
        # it sets that name in the mutual data and opens it using the openfile function. and then shows it
        # in the dictionary aswell. and saves to the log.  

        fname, _ = QFileDialog.getOpenFileName(sw,"Select file","dictionaries","Text files (*.txt)")
        print(fname+" MWF Line 2101")

        if fname != "":
            mutualData.directoryname = fname
            print(mutualData.directoryname + " MWF Line 2105")
            mutualData.currentdictionary = mainFunctions.useDir(mutualData.directoryname)
            mutualData.filename = os.path.basename(mutualData.directoryname)
            sw.l2.setText(md.filename)

            dictionaryW
            _,newdir = dictionaryW.openfile(fname)

            dictionaryW.oldname = dictionaryW.file_name

            dictionaryW.directory = fname
            dictionaryW.file_name = os.path.basename(fname)
            dictionaryW.currDictionaryLabelName.setText(dictionaryW.file_name)

            dictionaryW.tempdictforsave.clear()
            tdictsave = str(newdir)
            tdictsave = tdictsave.replace(", '{",",\n '{")
            for i in tdictsave.split("\n"):
                dictionaryW.tempdictforsave.append(i)
            dictionaryW.st = ""
            for i in dictionaryW.tempdictforsave:
                dictionaryW.st += i

            dictionaryW.showupdateddic(dictionaryW.tempdictforsave)
            mainFunctions.saveLog(("Changed default dictionary from settings to: " + mutualData.filename))

    def changedictionaryonstart(self):

        #Same function as the changedictionaryinsettings one, but it works on start of the app, incase the defaultDictionary
        # has been changed previously. 

        print(mutualData.directoryname + " MWF Line 2136")
        mutualData.currentdictionary = mainFunctions.useDir(mutualData.directoryname)
        mutualData.filename = os.path.basename(mutualData.directoryname)
        sw.l2.setText(md.filename)

        dictionaryW
        _,newdir = dictionaryW.openfile(mutualData.directoryname)

        dictionaryW.oldname = dictionaryW.file_name

        dictionaryW.directory = mutualData.directoryname
        dictionaryW.file_name = os.path.basename(mutualData.directoryname)
        dictionaryW.currDictionaryLabelName.setText(dictionaryW.file_name)

        dictionaryW.tempdictforsave.clear()
        tdictsave = str(newdir)
        tdictsave = tdictsave.replace(", '{",",\n '{")
        for i in tdictsave.split("\n"):
            dictionaryW.tempdictforsave.append(i)
        dictionaryW.st = ""
        for i in dictionaryW.tempdictforsave:
            dictionaryW.st += i

        dictionaryW.showupdateddic(dictionaryW.tempdictforsave)



    def getKey(self,val):

        #Gets the key of the element by value in dictionary.
    
        for key, value in mainFunctions.gardinersCodetoSymbolsf.items():
            if val == value:
                return key
    
        return "-"

    def hierotogard(self,text):

        #To translate from hiero to gardiners code, we just call the getKey function and retuns the key.

        new = ""
        text = text.replace(" ","")
        for i in text:
            value = self.getKey(i)
            new += value + " "
            
        return new

    def gardtohiero(self,text):

        #To get the hieroglyph from gardiners code, we make sure it isnt empty, then we just search for it and returns it.

        new = ""
        for i in text.split(" "):
            if i != "":
                if len(i) >= 2:
                    if i[0].lower() == "a" and i[1].lower() == "a":
                        i = i[0].upper() + i[1].lower() + i[2:]
                        
                        value = mainFunctions.gardinersCodetoSymbolsf.get(i,"-")
                        new += value + " "
                    else:
                        value = mainFunctions.gardinersCodetoSymbolsf.get(i.upper(),"-")
                        new += value + " "
            
        return new

    def textResultChange(self):

        #We just call the function of the corrosponding selected value of 
        # the combobox and return the translated text using its function.

        if ((self.langComboBox.currentText() == " English" or
              self.langComboBox.currentText() == " الإنجليزية") and
             (self.langComboBox_2.currentText() == " English" or
               self.langComboBox_2.currentText() == " الإنجليزية") and
               self.en_arTextEdit.toPlainText() != ""):
            self.hieroTextEdit_2.setPlainText(self.en_arTextEdit.toPlainText())

            mi.textEdit.setPlainText("")
            mr.textedit.setPlainText("")
        
        if ((self.langComboBox.currentText() == " English" or
              self.langComboBox.currentText() == " الإنجليزية") and
             (self.langComboBox_2.currentText() == " Hieroglyph" or
               self.langComboBox_2.currentText() == " الهيروغليفية") and
               self.en_arTextEdit.toPlainText() != ""):
            
            print(self.en_arTextEdit.toPlainText())
            moreinfo,foundforgard,transl,hiero = (
                mainFunctions.newSearchForEng(self.en_arTextEdit.toPlainText(), mutualData.currentdictionary))

            self.hieroTextEdit_2.setPlainText(hiero)
            mi.textEdit.setPlainText(moreinfo)
            mr.textedit.setPlainText("")

        if ((self.langComboBox.currentText() == " English" or
              self.langComboBox.currentText() == " الإنجليزية") and
             (self.langComboBox_2.currentText() == " Transliteration" or
               self.langComboBox_2.currentText() == " حرفي") and
               self.en_arTextEdit.toPlainText() != ""):
            
            print(self.en_arTextEdit.toPlainText())
            moreinfo,foundforgard,transl,hiero = (
                mainFunctions.newSearchForEng(self.en_arTextEdit.toPlainText(), mutualData.currentdictionary))
            
            transl = transl.replace("[","")
            transl = transl.replace("]"," ")

            self.hieroTextEdit_2.setPlainText(transl)
            mi.textEdit.setPlainText(moreinfo)
            mr.textedit.setPlainText("")
        
        if ((self.langComboBox.currentText() == " English" or
              self.langComboBox.currentText() == " الإنجليزية") and
             (self.langComboBox_2.currentText() == " Gardners code" or
               self.langComboBox_2.currentText() == " كود غاردينر") and
               self.en_arTextEdit.toPlainText() != ""):

            print(self.en_arTextEdit.toPlainText())
            moreinfo,foundforgard,transl,hiero = (
                mainFunctions.newSearchForEng(self.en_arTextEdit.toPlainText(), mutualData.currentdictionary))
            
            foundforgard = foundforgard.replace("{","")
            foundforgard = foundforgard.replace("}"," ")

            self.hieroTextEdit_2.setPlainText(foundforgard)
            mi.textEdit.setPlainText(moreinfo)
            mr.textedit.setPlainText("")
        
        
        
        if ((self.langComboBox.currentText() == " Hieroglyph" or
              self.langComboBox.currentText() == " الهيروغليفية") and
            (self.langComboBox_2.currentText() == " Hieroglyph" or
              self.langComboBox_2.currentText() == " الهيروغليفية") and
            self.en_arTextEdit.toPlainText() != ""):

            self.hieroTextEdit_2.setPlainText(self.en_arTextEdit.toPlainText())

        if ((self.langComboBox.currentText() == " Hieroglyph" or
              self.langComboBox.currentText() == " الهيروغليفية") and
            (self.langComboBox_2.currentText() == " English" or
              self.langComboBox_2.currentText() == " الإنجليزية") and
            self.en_arTextEdit.toPlainText() != ""):

            moreinfo,foundforgard,transl,hiero,finalsen,moreres = (mainFunctions.newSearchForHiero(self.en_arTextEdit.toPlainText(),mutualData.currentdictionary))
            print(moreinfo,foundforgard,transl,hiero,finalsen)

            finalsen = finalsen.replace("   "," ")
            finalsen = finalsen.replace("  "," ")
            if len(finalsen) != 0:
                if finalsen[0] == " ":
                    finalsen = finalsen[1:-1]

            self.hieroTextEdit_2.setPlainText(finalsen)
            mi.textEdit.setPlainText(moreinfo)
            mr.textedit.setPlainText(moreres)

        if ((self.langComboBox.currentText() == " Hieroglyph" or
              self.langComboBox.currentText() == " الهيروغليفية") and
            (self.langComboBox_2.currentText() == " Transliteration" or
              self.langComboBox_2.currentText() == " حرفي") and
            self.en_arTextEdit.toPlainText() != ""):

            moreinfo,foundforgard,transl,hiero,finalsen,moreres = (mainFunctions.newSearchForHiero(self.en_arTextEdit.toPlainText(),mutualData.currentdictionary))
            print(moreinfo,foundforgard,transl,hiero,finalsen)

            transl = transl.replace("[","")
            transl = transl.replace("]"," ")

            self.hieroTextEdit_2.setPlainText(transl)
            mi.textEdit.setPlainText(moreinfo)

        if ((self.langComboBox.currentText() == " Hieroglyph" or
              self.langComboBox.currentText() == " الهيروغليفية") and
             (self.langComboBox_2.currentText() == " Gardners code" or
               self.langComboBox_2.currentText() == " كود غاردينر") and
               self.en_arTextEdit.toPlainText() != "") :
            
            print(self.en_arTextEdit.toPlainText())
            self.hieroTextEdit_2.setPlainText( self.hierotogard(self.en_arTextEdit.toPlainText()))



        if ((self.langComboBox.currentText() == " Gardners code" or
              self.langComboBox.currentText() == " كود غاردينر") and
            (self.langComboBox_2.currentText() == " Gardners code" or
              self.langComboBox_2.currentText() == " كود غاردينر") and
            self.en_arTextEdit.toPlainText() != ""):

            self.hieroTextEdit_2.setPlainText(self.en_arTextEdit.toPlainText())
            
        if ((self.langComboBox.currentText() == " Gardners code" or
              self.langComboBox.currentText() == " كود غاردينر") and
            (self.langComboBox_2.currentText() == " English" or
              self.langComboBox_2.currentText() == " الإنجليزية") and
            self.en_arTextEdit.toPlainText() != ""):

            moreinfo,foundforgard,transl,hiero,finalsen,moreres = (mainFunctions.newSearchForGard(self.gardtohiero(self.en_arTextEdit.toPlainText()),mutualData.currentdictionary))
            print(moreinfo,foundforgard,transl,hiero,finalsen)

            finalsen = finalsen.replace("   "," ")
            finalsen = finalsen.replace("  "," ")
            print(finalsen + "line 2342")

            if finalsen != "":
                if finalsen[0] == " ":
                    finalsen = finalsen[1:-1]

                self.hieroTextEdit_2.setPlainText(finalsen)
                mi.textEdit.setPlainText(moreinfo)
                mr.textedit.setPlainText(moreres)

        if ((self.langComboBox.currentText() == " Gardners code" or
              self.langComboBox.currentText() == " كود غاردينر") and
            (self.langComboBox_2.currentText() == " Transliteration" or
              self.langComboBox_2.currentText() == " حرفي") and
            self.en_arTextEdit.toPlainText() != ""):

            moreinfo,foundforgard,transl,hiero,finalsen,moreres = (mainFunctions.newSearchForGard(self.gardtohiero(self.en_arTextEdit.toPlainText()),mutualData.currentdictionary))
            print(moreinfo,foundforgard,transl,hiero,finalsen)

            transl = transl.replace("[","")
            transl = transl.replace("]"," ")

            self.hieroTextEdit_2.setPlainText(transl)
            mi.textEdit.setPlainText(moreinfo)
            mr.textedit.setPlainText(moreres)

        if ((self.langComboBox.currentText() == " Gardners code" or
              self.langComboBox.currentText() == " كود غاردينر") and
             (self.langComboBox_2.currentText() == " Hieroglyph" or
               self.langComboBox_2.currentText() == " الهيروغليفية") and
               self.en_arTextEdit.toPlainText() != "") :
            
            print(self.en_arTextEdit.toPlainText())
            self.hieroTextEdit_2.setPlainText( self.gardtohiero(self.en_arTextEdit.toPlainText()))



        if ((self.langComboBox.currentText() == " Transliteration" or
              self.langComboBox.currentText() == " حرفي") and
            (self.langComboBox_2.currentText() == " Transliteration" or
              self.langComboBox_2.currentText() == " حرفي") and
            self.en_arTextEdit.toPlainText() != ""):

            self.hieroTextEdit_2.setPlainText(self.en_arTextEdit.toPlainText())
            mr.textedit.setPlainText("")
            mi.textEdit.setPlainText("")

        if ((self.langComboBox.currentText() == " Transliteration" or
              self.langComboBox.currentText() == " حرفي") and
            (self.langComboBox_2.currentText() == " Gardners code" or
              self.langComboBox_2.currentText() == " كود غاردينر") and
            self.en_arTextEdit.toPlainText() != ""):

            print(self.en_arTextEdit.toPlainText())
            moreinfo, foundforgard, eng, hiero = (
            mainFunctions.newSearchForTransl(self.en_arTextEdit.toPlainText(), mutualData.currentdictionary))
            
            foundforgard = foundforgard.replace("{","")
            foundforgard = foundforgard.replace("}"," ")

            self.hieroTextEdit_2.setPlainText(foundforgard)
            mi.textEdit.setPlainText(moreinfo)
            mr.textedit.setPlainText("")
        
        if ((self.langComboBox.currentText() == " Transliteration" or
              self.langComboBox.currentText() == " حرفي") and
            (self.langComboBox_2.currentText() == " English" or
              self.langComboBox_2.currentText() == " الإنجليزية") and
            self.en_arTextEdit.toPlainText() != ""):

            moreinfo, foundforgard, eng, hiero = (mainFunctions.newSearchForTransl(self.en_arTextEdit.toPlainText(),mutualData.currentdictionary))
            print(moreinfo, foundforgard, eng, hiero)

            eng = eng.replace("   "," ")
            eng = eng.replace("  "," ")
            if len(eng) != 0:
                if eng[0] == " ":
                    eng = eng[1:-1]


            self.hieroTextEdit_2.setPlainText(eng)
            mi.textEdit.setPlainText(moreinfo)
            mr.textedit.setPlainText("")

        if ((self.langComboBox.currentText() == " Transliteration" or
              self.langComboBox.currentText() == " حرفي") and
            (self.langComboBox_2.currentText() == " Hieroglyph" or
              self.langComboBox_2.currentText() == " الهيروغليفية") and
            self.en_arTextEdit.toPlainText() != ""):


            moreinfo, foundforgard, eng, hiero = (mainFunctions.newSearchForTransl(self.en_arTextEdit.toPlainText(),mutualData.currentdictionary))
            print(moreinfo, foundforgard, eng, hiero)


            self.hieroTextEdit_2.setPlainText(hiero)
            mi.textEdit.setPlainText(moreinfo)
            mr.textedit.setPlainText("")

        if ((self.langComboBox.currentText() == " Names (English)" or 
        self.langComboBox.currentText() == " اسماء (الإنجليزية)") and
        (self.langComboBox_2.currentText() == " Hieroglyph" or
        self.langComboBox_2.currentText() == " الهيروغليفية") and
        self.en_arTextEdit.toPlainText() != ""):

        
            enname = mainFunctions.namefinder(self.en_arTextEdit.toPlainText(),mainFunctions.dictionaryForNamesEn)
            self.hieroTextEdit_2.setPlainText(enname)
            mi.textEdit.setPlainText("")
            mr.textedit.setPlainText("")
        
        if ((self.langComboBox.currentText() == " Names (English)" or 
        self.langComboBox.currentText() == " اسماء (الإنجليزية)") and
        self.langComboBox_2.currentIndex() == 0 and
        self.en_arTextEdit.toPlainText() != ""):
            
            self.hieroTextEdit_2.setPlainText("")

        if ((self.langComboBox.currentText() == " Names (English)" or 
        self.langComboBox.currentText() == " اسماء (الإنجليزية)") and
        self.langComboBox_2.currentIndex() == 2 and
        self.en_arTextEdit.toPlainText() != ""):
            
            self.hieroTextEdit_2.setPlainText("")

        if ((self.langComboBox.currentText() == " Names (English)" or 
        self.langComboBox.currentText() == " اسماء (الإنجليزية)") and
        self.langComboBox_2.currentIndex() == 3 and
        self.en_arTextEdit.toPlainText() != ""):
            
            self.hieroTextEdit_2.setPlainText("")

        if ((self.langComboBox.currentText() == " Names (Arabic)" or 
        self.langComboBox.currentText() == " اسماء (العربية)") and
        (self.langComboBox_2.currentText() == " Hieroglyph" or
        self.langComboBox_2.currentText() == " الهيروغليفية") and
        self.en_arTextEdit.toPlainText() != ""):

        
            arname = mainFunctions.namefinder(self.en_arTextEdit.toPlainText(),mainFunctions.dictionaryForNamesAr)
            self.hieroTextEdit_2.setPlainText(arname)
            mi.textEdit.setPlainText("")
            mr.textedit.setPlainText("")

        if ((self.langComboBox.currentText() == " Names (Arabic)" or 
        self.langComboBox.currentText() == " اسماء (العربية)") and
        self.langComboBox_2.currentIndex() == 0 and
        self.en_arTextEdit.toPlainText() != ""):
            
            self.hieroTextEdit_2.setPlainText("")
            
        if ((self.langComboBox.currentText() == " Names (Arabic)" or 
        self.langComboBox.currentText() == " اسماء (العربية)") and
        self.langComboBox_2.currentIndex() == 2 and
        self.en_arTextEdit.toPlainText() != ""):
            
            self.hieroTextEdit_2.setPlainText("")

        if ((self.langComboBox.currentText() == " Names (Arabic)" or 
        self.langComboBox.currentText() == " اسماء (العربية)") and
        self.langComboBox_2.currentIndex() == 3 and
        self.en_arTextEdit.toPlainText() != ""):
            
            self.hieroTextEdit_2.setPlainText("")


        if self.en_arTextEdit.toPlainText() == "":
            self.hieroTextEdit_2.setPlainText("")
            mi.textEdit.setPlainText("")
            mr.textedit.setPlainText("")

        self.hieroTextEdit_2.moveCursor(QtGui.QTextCursor.End)

        mutualData.combo1 = self.langComboBox.currentIndex()
        mutualData.combo2 = self.langComboBox_2.currentIndex()

    def displayTime(self):

        #Make an element of QTime and QDate and shows it in the time and date label.

        time = QtCore.QTime.currentTime().toString("h:mm:ss AP")
        self.timeLabel.setText(time)
        date = QtCore.QDate.currentDate().toString('dd/MM/yyyy')
        self.dateLabel.setText(date)



    def changeTextSize(self):

        #A function that changes the text edits font size according to the current comboboxes.
        # if its hieroglyph then it increases the size, it its english it returns it to the normal size,
        # if its gardiners code it increases its size, but not as big as the hieroglyph one,
        # and lastly for transliteration it increases the size and changes the font aswell.   
        
        if self.langComboBox.currentText() == " Hieroglyph" or self.langComboBox.currentText() == " الهيروغليفية":
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(32)
            font.setBold(False)
            font.setWeight(50)
            self.en_arTextEdit.setFont(font)
        if self.langComboBox.currentText() == " English" or self.langComboBox.currentText() == " الإنجليزية":
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(16)
            font.setBold(False)
            font.setWeight(50)
            self.en_arTextEdit.setFont(font)
        if self.langComboBox.currentText() == " Transliteration" or self.langComboBox.currentText() == " حرفي":
            font = QtGui.QFont()
            font.setFamily("Transliteration")
            font.setPointSize(22)
            font.setBold(True)
            font.setWeight(50)
            self.en_arTextEdit.setFont(font)
        if self.langComboBox.currentText() == " Gardners code" or self.langComboBox.currentText() == " كود غاردينر":
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(50)
            self.en_arTextEdit.setFont(font)
            self.hieroTextEdit_2.setText("")

        if self.langComboBox_2.currentText() == " Hieroglyph" or self.langComboBox_2.currentText() == " الهيروغليفية":
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(32)
            font.setBold(True)
            font.setWeight(50)
            self.hieroTextEdit_2.setFont(font)
        if self.langComboBox_2.currentText() == " English" or self.langComboBox_2.currentText() == " الإنجليزية":
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(50)
            self.hieroTextEdit_2.setFont(font)
        if self.langComboBox_2.currentText() == " Gardners code" or self.langComboBox_2.currentText() == " كود غاردينر":
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(50)
            self.hieroTextEdit_2.setFont(font)
        if self.langComboBox_2.currentText() == " Transliteration" or self.langComboBox_2.currentText() == " حرفي":
            font = QtGui.QFont()
            font.setFamily("Transliteration")
            font.setPointSize(22)
            font.setBold(True)
            font.setWeight(50)
            self.hieroTextEdit_2.setFont(font)
        
        self.textResultChange()

    def minimizeWindow(self):
        self.showMinimized()

    def exitWindow(self):

        #Exit just saves to log and quits the application.

        mainFunctions.saveLog("Closed Ankh the application.")
        QtWidgets.QApplication.instance().quit()

        

    def writeb(self, _str):

        #writeb function writes the current clicked hieroglyph button into the text edit and moves the cursor to the end.

        t = self.en_arTextEdit.toPlainText()
        new = t + _str + " "
        self.en_arTextEdit.setPlainText(new)
        self.en_arTextEdit.moveCursor(QtGui.QTextCursor.End)
        print(_str + " MWF Line 2613")    

    def makebtn(self, name, sign, j, i):

        #This functions makes the actual hieroglyph buttons, it takes the name and sign and the position
        # of where the button should be as arguements. It names the buttons and gives it functionality,
        # their functions are the writeb function. and it also sets the tooltip with the gardiners code of the symbol.  

        naming = str(name)
        name = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        name.setMinimumSize(QtCore.QSize(64, 64))
        name.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Egyptian Hieroglyphs")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        name.setFont(font)

        if mutualData.btncolors == "w":
            name.setStyleSheet("""QPushButton{color: rgb(0, 0, 0)}
            QPushButton:pressed{background-color: rgba(25, 25, 25,50);}""")
        elif mutualData.btncolors == "d":
            name.setStyleSheet("""QPushButton{color: rgb(255, 255, 255)}
            QPushButton:pressed{background-color: rgba(25, 25, 25,50);}""")
        name.setFlat(True)
        name.setObjectName(naming)
        name.setToolTip(naming)
        name.setText(sign)
        self.gridLayout_2.addWidget(name, j, i, 1, 1)
        #self.b1.clicked.connect(lambda: writeb(signname))
        name.clicked.connect(lambda: self.writeb(sign))
            
    def btnmaker(self, hierocategory):

        #This function creates a category's buttons, it takes the categories name as an arguement. and it goes
        # through a nested loop to create the buttons per line, then goes onto the next line and so on. 

        tempsign = []
        tempgard = []
        

        for gard, sign in hierocategory.items():
            tempgard.append(gard)
            tempsign.append(sign)

        cc = 0
        tot = -(len(tempsign)//-18)
        if len(tempsign) > 18:
            for j in range(tot):

                
                for i in range(18):
                    if cc <= (len(tempsign)-1):
                        gardname = tempgard[cc]
                        signname = tempsign[cc]

                        self.makebtn(gardname, signname , j, i)
                        
                        cc += 1
        
        else:
            for i in range(24):
                    if cc <= (len(tempsign)-1):
                        gardname = tempgard[cc]
                        signname = tempsign[cc]

                        self.makebtn(gardname, signname , 1, i)

                        cc += 1    

    def btnmakerall(self):
        
        #This function just creates all the buttons using the main hieroglyph dictionary, similarly to the previous function
        # except it isnt just 1 category, but all the dictionary. 

        tempsign = []
        tempgard = []
        tempbtns = {}

        for gard, sign in mainFunctions.gardinersCodetoSymbolsf.items():
            tempgard.append(gard)
            tempsign.append(sign)

        cc = 0
        tot = -(len(tempsign)//-18)
        if len(tempsign) > 18:
            for j in range(tot):

                
                for i in range(18):
                    if cc <= (len(tempsign)-1):
                        gardname = tempgard[cc]
                        signname = tempsign[cc]

                        self.makebtn(gardname, signname , j, i)


                        cc += 1
        for i in tempbtns.items():
            print(str(i) + " MWF Line 2713")
            
        #print(str(len(tempbtns)) + " MWF Line 2715") 

    def widdel(self):

        #This function deletes the scrollArea widget, so when we change the category it deletes the current widget,
        # and remakes it again, not to overwrite the current existing elements. 

        self.gridLayout_2.removeWidget(self.scrollAreaWidgetContents_2)
        self.scrollAreaWidgetContents_2.deleteLater()
        self.scrollAreaWidgetContents_2 = None

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1187, 197))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
    
    def combochange(self):

        #this function uses the widdel function and the btnmaker functions according to the selected combobox element,
        # it all signs is set, it uses the btnmakerall function, else it uses the btnmaker function with the selected
        # category, using the dictionary variables we had earlier using the formater function.  


        
        if self.categoryComboBox.currentText() == "-. All signs" or self.categoryComboBox.currentText() == "-. كل الرموز":
            self.widdel()
            self.btnmakerall()
        elif self.categoryComboBox.currentText() == "A. Man and his Occupations" or self.categoryComboBox.currentText() == "A. الرجل ومهنه":
            self.widdel()
            self.btnmaker(self.a)
        elif self.categoryComboBox.currentText() == "B. Woman and her Occupations" or self.categoryComboBox.currentText() == "B. المرأة ومهنها":
            self.widdel()
            self.btnmaker(self.b)
        elif self.categoryComboBox.currentText() == "C. Anthropomorphic Deities" or self.categoryComboBox.currentText() == "C. مجسم الآلهة":
            self.widdel()
            self.btnmaker(self.c)
        elif self.categoryComboBox.currentText() == "D. Parts of the Human Body" or self.categoryComboBox.currentText() == "D. اجزاء من جسم الانسان":
            self.widdel()
            self.btnmaker(self.d)
        elif self.categoryComboBox.currentText() == "E. Mammals" or self.categoryComboBox.currentText() == "E. الثدييات":
            self.widdel()
            self.btnmaker(self.e)
        elif self.categoryComboBox.currentText() == "F. Parts of Mammals" or self.categoryComboBox.currentText() == "F. أجزاء من الثدييات":
            self.widdel()
            self.btnmaker(self.f)
        elif self.categoryComboBox.currentText() == "G. Birds" or self.categoryComboBox.currentText() == "G. طيور":
            self.widdel()
            self.btnmaker(self.g)
        elif self.categoryComboBox.currentText() == "H. Parts of Birds" or self.categoryComboBox.currentText() == "H. اجزاء من الطيور":
            self.widdel()
            self.btnmaker(self.h)
        elif self.categoryComboBox.currentText() == "I. Amphibious Animals, Reptiles, etc." or self.categoryComboBox.currentText() == "I. الحيوانات البرمائية والزواحف وما إلى ذلك":
            self.widdel()
            self.btnmaker(self.i)
        elif self.categoryComboBox.currentText() == "K. Fish and Parts of Fish" or self.categoryComboBox.currentText() == "K. الأسماك وأجزاء من الأسماك":
            self.widdel()
            self.btnmaker(self.k)
        elif self.categoryComboBox.currentText() == "L. Invertebrates and Lesser Animals" or self.categoryComboBox.currentText() == "L. اللافقاريات والحيوانات الصغرى":
            self.widdel()
            self.btnmaker(self.l)
        elif self.categoryComboBox.currentText() == "M. Trees and Plants" or self.categoryComboBox.currentText() == "M. الأشجار والنباتات":
            self.widdel()
            self.btnmaker(self.m)
        elif self.categoryComboBox.currentText() == "N. Sky, Earth, Water" or self.categoryComboBox.currentText() == "N. السماء والأرض والمياه":
            self.widdel()
            self.btnmaker(self.n)
        elif self.categoryComboBox.currentText() == "O. Buildings, Parts of Buildings, etc." or self.categoryComboBox.currentText() == "O. المباني ، أجزاء المباني ، إلخ":
            self.widdel()
            self.btnmaker(self.o)
        elif self.categoryComboBox.currentText() == "P. Ships and Parts of Ships" or self.categoryComboBox.currentText() == "P. السفن وأجزاء السفن":
            self.widdel()
            self.btnmaker(self.p)
        elif self.categoryComboBox.currentText() == "Q. Domestics and Funerary Furniture" or self.categoryComboBox.currentText() == "Q. أثاث المنازل والجنائز":
            self.widdel()
            self.btnmaker(self.q)
        elif self.categoryComboBox.currentText() == "R. Temple Furniture and Sacred Emblems" or self.categoryComboBox.currentText() == "R. أثاث المعبد والشعارات المقدسة":
            self.widdel()
            self.btnmaker(self.r)
        elif self.categoryComboBox.currentText() == "S. Crowns, Dress, Staves, etc." or self.categoryComboBox.currentText() == "S. التيجان ، اللباس ، العصي ، إلخ":
            self.widdel()
            self.btnmaker(self.s)
        elif self.categoryComboBox.currentText() == "T. Warfare, Hunting, Butchery" or self.categoryComboBox.currentText() == "T. حرب ، صيد ، مجزرة":
            self.widdel()
            self.btnmaker(self.t)
        elif self.categoryComboBox.currentText() == "U. Agriculture, Crafts, and Professions" or self.categoryComboBox.currentText() == "U. الزراعة والحرف والمهن":
            self.widdel()
            self.btnmaker(self.u)
        elif self.categoryComboBox.currentText() == "V. Rope, Fiber, Baskets, Bags, etc." or self.categoryComboBox.currentText() == "V. حبل ، ألياف ، سلال ، أكياس ، إلخ":
            self.widdel()
            self.btnmaker(self.v)
        elif self.categoryComboBox.currentText() == "W. Vessels of Stone and Earthenware" or self.categoryComboBox.currentText() == "W. السفن الحجرية والخزفية":
            self.widdel()
            self.btnmaker(self.w)
        elif self.categoryComboBox.currentText() == "X. Loaves and Cakes" or self.categoryComboBox.currentText() == "X. أرغفة وكعك":
            self.widdel()
            self.btnmaker(self.x)
        elif self.categoryComboBox.currentText() == "Y. Writings, Games, Music" or self.categoryComboBox.currentText() == "Y. كتابات ، ألعاب ، موسيقى":
            self.widdel()
            self.btnmaker(self.y)
        elif self.categoryComboBox.currentText() == "Z. Strokes, Signs derived from Hieratic, Geometrical Figures" or self.categoryComboBox.currentText() == "Z. العلامات مشتقة من الأشكال الهيراطيقية والهندسية":
            self.widdel()
            self.btnmaker(self.z)
        elif self.categoryComboBox.currentText() == "Aa. Unclassified" or self.categoryComboBox.currentText() == "Aa. غير مصنف":
            self.widdel()
            self.btnmaker(self.aa)

        """A. Man and his Occupations
            B. Woman and her Occupations
            C. Anthropomorphic Deities
            D. Parts of the Human Body
            E. Mammals
            F. Parts of Mammals
            G. Birds
            H. Parts of Birds
            I. Amphibious Animals, Reptiles, etc.
            K. Fish and Parts of Fish
            L. Invertebrates and Lesser Animals
            M. Trees and Plants
            N. Sky, Earth, Water
            O. Buildings, Parts of Buildings, etc.
            P. Ships and Parts of Ships
            Q. Domestics and Funerary Furniture
            R. Temple Furniture and Sacred Emblems
            S. Crowns, Dress, Staves, etc.
            T. Warfare, Hunting, Butchery
            U. Agriculture, Crafts, and Professions
            V. Rope, Fiber, Baskets, Bags, etc.
            W. Vessels of Stone and Earthenware
            X. Loaves and Cakes
            Y. Writings, Games, Music
            Z. Strokes, Signs derived from Hieratic, Geometrical Figures
            Aa. Unclassified"""    
        

    def mrshowhide(self):
        mr.hide()
        mr.show()

    def mishowhide(self):
        mi.hide()
        mi.show()

    def guideshowhide(self):
        guide.hide()
        guide.show()

    def dicshowhide(self):
        dictionaryW.hide()
        dictionaryW.show()




    #The following functions record mouse press, move and release events. which gives control
    # to be able to drag the main gui around. 

    offset = QtCore.QPoint(642, 316)
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
            print(str(self.offset) + " MWF Line 2862")
        else:
            super().mousePressEvent(event)
    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)
    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)



app = QtWidgets.QApplication(sys.argv)
myWindow = MyWin()
myWindow.show()
app.exec_()