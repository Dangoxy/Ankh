import ctypes
from dictionaryWindow import *
from addWindow import *
from addWindow import Ui_addWindow
import sys
import ast
from PyQt5.QtCore import QTimer
from PyQt5 import sip
from PyQt5.QtWidgets import QFileDialog
import os
from mutualData import mutualData
import mainFunctions
from addFunctions import addFunctions
from mutualData import mutualData

class dictionaryFunctions(QtWidgets.QMainWindow, Ui_dictionaryWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

        self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint, True)


        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        self.setWindowIcon(QtGui.QIcon(
            ':icons\\icons\\ankh_icon.png'))

        global addWindow
        addWindow = QtWidgets.QMainWindow()
        addui = Ui_addWindow()
        addui.setupUi(addWindow)

        global addW
        addW = addFunctions()

        
        self.tempdictforsave = []
        self.st = ""
        self.timer = QTimer()

        self.directory = mutualData.directoryname
        self.file_name = os.path.basename(mutualData.directoryname)
        self.currDictionaryLabelName.setText(self.file_name)

        self.showdic(self.directory)
        listofd,self.atss = self.openfile(self.directory)
        
        self.addBtn.clicked.connect(lambda: (self.addopenfunc()))
        self.removeBtn.clicked.connect(lambda: (self.removeSelectedItem(self.atss)))
        self.saveAsBtn.clicked.connect(lambda: (self.newsaveas()))
        self.saveBtn.clicked.connect(lambda: (self.newsave()))
        self.changeDictionaryBtn.clicked.connect(lambda: (self.changeDictionary()))
        self.listWidget.itemChanged.connect(lambda: (self.itemEdited()))




        


    def changeDictionary(self):

        #Same function used in the main GUI.

        fname, _ = QFileDialog.getOpenFileName(self,"Select file","dictionaries","Text files (*.txt)")
        print(fname + " DF Line 69")

        if fname != "":

            _,newdir = self.openfile(fname)

            self.oldname = self.file_name

            self.directory = fname
            self.file_name = os.path.basename(fname)
            self.currDictionaryLabelName.setText(self.file_name)

            mutualData.directoryname = fname
            print(mutualData.directoryname+ " DF Line 82")
            mutualData.currentdictionary = mainFunctions.useDir(mutualData.directoryname)
            mutualData.filename = os.path.basename(mutualData.directoryname)


            self.tempdictforsave.clear()
            tdictsave = str(newdir)
            tdictsave = tdictsave.replace(", '{",",\n '{")
            for i in tdictsave.split("\n"):
                self.tempdictforsave.append(i)
            self.st = ""
            for i in self.tempdictforsave:
                self.st += i

            self.showupdateddic(self.tempdictforsave)


            self.statusLabel.setText("Dictionary changed from: (" + self.oldname + ") To: (" + self.file_name + ")")
            self.statusLabel.setStyleSheet("color:rgb(55,255,55)")
            self.timer.start(5000)
            self.timer.timeout.connect(lambda: self.timeoutForDict())
            mainFunctions.saveLog("Changed dictionary from: " +self.oldname + ", to: " + self.file_name)
        
        else: 
            print("canceled"+ " DF Line 106")

    def save(self,atss):

        #Takes data from the list widget, and saves it into a text file to use as the main dictionary.

        if len(self.tempdictforsave) == 0:
            new = ast.literal_eval(atss)
        elif len(self.tempdictforsave) != 0:
            new = ast.literal_eval(self.st)

        self.tempdictforsave.clear()
        tdictsave = str(new)
        tdictsave = tdictsave.replace(", '{",",\n '{")
        for i in tdictsave.split("\n"):
                self.tempdictforsave.append(i)
        self.st = ""
        for i in self.tempdictforsave:
            self.st += i

        with open(self.directory,"w") as f:
            f.write(tdictsave)

        self.changeStatusIconSaved()
        print(self.tempdictforsave[0] + " DF Line 130")

        self.statusLabel.setText("File as been saved successfully.")
        self.statusLabel.setStyleSheet("color:rgb(55,255,55)")
        self.timer.start(5000)
        self.timer.timeout.connect(lambda: self.timeoutForDict())
        mainFunctions.saveLog("Saved dictionary.")

    def newsave(self):

        items = []
        for x in range(self.listWidget.count()):
            items.append(self.listWidget.item(x).text())

        stitems = ""

        for i in items:
            stitems += i
            
        stitems = stitems.replace(",'{",",\n '{")

        with open(self.directory,"w") as f:
            f.write(str(stitems))

        mutualData.currentdictionary = mainFunctions.useDir(mutualData.directoryname)

        self.changeStatusIconSaved()
        
    	    
        self.statusLabel.setText("File as been saved successfully.")
        self.statusLabel.setStyleSheet("color:rgb(55,255,55)")
        self.timer.start(5000)
        self.timer.timeout.connect(lambda: self.timeoutForDict())
        mainFunctions.saveLog("Saved dictionary.")



        self.showupdateddic(items)
        
    def newsaveas(self):
        #Same function as the save, but it takes a file name from the user to save it as said name.

        fname, _ = QFileDialog.getSaveFileName(self,"Save as","dictionaries","Text files (*.txt)")
        print(fname+ " DF Line 173")

        if fname != "":

            items = []
            for x in range(self.listWidget.count()):
                items.append(self.listWidget.item(x).text())

            stitems = ""

            for i in items:
                stitems += i
                
            stitems = stitems.replace(",'{",",\n '{")


            with open(fname,"w") as f:
                f.write(str(stitems))


            self.directory = fname
            self.file_name = os.path.basename(self.directory)
            self.currDictionaryLabelName.setText(self.file_name)

            mutualData.directoryname = fname
            print(mutualData.directoryname+ " DF Line 198")
            mutualData.currentdictionary = mainFunctions.useDir(mutualData.directoryname)
            mutualData.filename = os.path.basename(mutualData.directoryname)

            self.changeStatusIconSaved()
            

            self.statusLabel.setText("File as been saved successfully.")
            self.statusLabel.setStyleSheet("color:rgb(55,255,55)")
            self.timer.start(5000)
            self.timer.timeout.connect(lambda: self.timeoutForDict())
            mainFunctions.saveLog("Saved dictionary.")

            self.showupdateddic(items)

        
        else:
            print("canceled"+ " DF Line 215")

    def itemEdited(self):

        #If an item is edited, it changes the status and says its edited.

        self.changeStatusIconPending()

        item = self.listWidget.currentItem()
        temp = item.text()
        b = temp.index("'{")
        e = temp.index("}'")
        changedKey = temp[b+1:e+1]

        print(temp+ " DF Line 229")
        

        self.newsave()
        self.statusLabel.setText("Item with key "+ changedKey +" edited.")
        self.statusLabel.setStyleSheet("color:rgb(55,55,255)")
        self.timer.start(5000)
        self.timer.timeout.connect(lambda: self.timeoutForDict())

    def changeStatusIconPending(self):
            
            #Changes the status label tool tip and icon.

            print("Changed"+ " DF Line 242")
            self.statusIconLabel.setText("⚫")
            self.statusIconLabel.setToolTip("Pending save.")

    def changeStatusIconSaved(self):

            #Changes the labels tool tip and icon.

            print("didnt change."+ " DF Line 250")
            self.statusIconLabel.setText("⚪")
            self.statusIconLabel.setToolTip("No change.")
    
    def saveAs(self,atss):

        #Same function as the save, but it takes a file name from the user to save it as said name.

        fname, _ = QFileDialog.getSaveFileName(self,"Save as","dictionaries","Text files (*.txt)")
        print(fname+ " DF Line 259")

        if fname != "":

            if len(self.tempdictforsave) == 0:
                new = ast.literal_eval(atss)
            elif len(self.tempdictforsave) != 0:
                new = ast.literal_eval(self.st)

            self.tempdictforsave.clear()
            tdictsave = str(new)
            tdictsave = tdictsave.replace(", '{",",\n '{")
            for i in tdictsave.split("\n"):
                self.tempdictforsave.append(i)
            self.st = ""
            for i in self.tempdictforsave:
                self.st += i

            with open(fname,"w") as f:
                f.write(tdictsave)

            self.directory = fname
            self.file_name = os.path.basename(self.directory)
            self.currDictionaryLabelName.setText(self.file_name)

            mutualData.directoryname = fname
            print(mutualData.directoryname+ " DF Line 285")
            mutualData.currentdictionary = mainFunctions.useDir(mutualData.directoryname)
            mutualData.filename = os.path.basename(mutualData.directoryname)

            self.changeStatusIconSaved()
            self.statusLabel.setText("File as been saved successfully.")
            self.statusLabel.setStyleSheet("color:rgb(55,255,55)")
            self.timer.start(5000)
            self.timer.timeout.connect(lambda: self.timeoutForDict())
            mainFunctions.saveLog(("Saved dictionary as: " + self.file_name))



        
        else:
            print("canceled"+ " DF Line 300")

    def timeoutForDict(self):

        #Returns the status label to its normal state.

        if not sip.isdeleted(self.statusLabel):
            if mutualData.btncolors == "w":
                self.statusLabel.setText("Status:-----------------------------------------------------------------------------------------------------")
                self.statusLabel.setStyleSheet("color: rgb(105, 105, 157);")
            else:
                self.statusLabel.setText("Status:-----------------------------------------------------------------------------------------------------")
                self.statusLabel.setStyleSheet("color: rgb(255, 255, 255);")
            self.timer.stop()

    def timeoutForAdd(self,addui):

        #Returns the add status label into its normal state.

        if not sip.isdeleted(addui.statusLabel):
            addui.statusLabel.setText("")
            self.timer.stop()

    def adduiuse(self):

        #Makes an object of addWindow for usage.

        global addWindow
        addWindow = QtWidgets.QMainWindow()
        
        addui = Ui_addWindow()
        addui.setupUi(addWindow)

        return addui

    def addBtnSingleMeaning(self, atss,addui):

        #Function for the add button, it takes the dictionary to save it to, and the add object.
        # It takes the info from the text edits and saves them to the dictionary. If something is empty,
        # it returns an error message in the status label.  
        
        if len(self.tempdictforsave) == 0:
            new = ast.literal_eval(atss)
        elif len(self.tempdictforsave) != 0:
            new = ast.literal_eval(self.st)
        
        g = addui.gardTextEditSing.toPlainText()
        tl = addui.translTextEditSing.toPlainText()
        t = addui.transTextEditSing.toPlainText()
        gw = "{" + g + "}"
        
        if (g != "" and tl != "" and t != ""):
            if  gw not in new:
                comb = "[" + addui.translTextEditSing.toPlainText() + "] " + addui.transTextEditSing.toPlainText()
                gard = "{" + addui.gardTextEditSing.toPlainText() + "}"
                #print(gard + ": "+ comb)
                new[gard] = comb



                addui.statusLabel.setText("Added successfully")
                addui.statusLabel.setStyleSheet("color:rgb(55,255,55)")
                addui.gardTextEditSing.setPlainText("")
                addui.translTextEditSing.setPlainText("")
                addui.transTextEditSing.setPlainText("")
                self.changeStatusIconPending()



                self.tempdictforsave.clear()
                tdictsave = str(new)
                tdictsave = tdictsave.replace(", '{",",\n '{")
                for i in tdictsave.split("\n"):
                    self.tempdictforsave.append(i)
                self.st = ""
                for i in self.tempdictforsave:
                    self.st += i
                self.showupdateddic(self.tempdictforsave)

                mainFunctions.saveLog(("Added a word with a single meaning with key: " + gard + "."))
                
                
                


            else:
                addui.statusLabel.setText("Key already exists.")
                addui.statusLabel.setStyleSheet("color:rgb(55,55,255)")

        else:
            addui.statusLabel.setText("Please fill all the fields.")
            addui.statusLabel.setStyleSheet("color:rgb(255,55,55)")


        self.timer.start(5000)
        self.timer.timeout.connect(lambda: self.timeoutForAdd(addui))

    def removeSelectedItem(self,atss):

        #Takes the currently selected item info and gets the key from it and removes it from the dictionary.

        bruh = ""
        if len(self.tempdictforsave) == 0:
            new = ast.literal_eval(atss)
        elif len(self.tempdictforsave) != 0:
            new = ast.literal_eval(self.st)

        selectedItem = self.listWidget.selectedItems()
        if not selectedItem: 
            return        
        for item in selectedItem:
            bruh =item.text() 
            print(bruh+ " DF Line 412")

        startIndex = bruh.index("'{")
        endIndex = bruh.index("}'")
        theKey = bruh[startIndex+1:endIndex+1]

        print(theKey+ " DF Line 418")
        del new[theKey]

        self.tempdictforsave.clear()
        tdictsave = str(new)
        tdictsave = tdictsave.replace(", '{",",\n '{")
        for i in tdictsave.split("\n"):
            self.tempdictforsave.append(i)
        self.st = ""
        for i in self.tempdictforsave:
            self.st += i

        self.showupdateddic(self.tempdictforsave)
        self.changeStatusIconPending()      

        self.statusLabel.setText("Item with key "+ theKey +" Has been removed.")
        self.statusLabel.setStyleSheet("color:rgb(255,55,55)")
        self.timer.start(5000)
        self.timer.timeout.connect(lambda: self.timeoutForDict())
        mainFunctions.saveLog("Removed a word with the key " + theKey + ".")
       
    def showupdateddic(self,tempdic):

        #Clears the list widget and shows the current dictionary again.

        self.listWidget.clear()
        for line in tempdic:
            
            item = QtWidgets.QListWidgetItem()
            
            line = line.replace("\n","")
            line = line.replace(" '{","'{")
            item.setText(str(line))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
            self.listWidget.addItem(item)

    def showdic(self,dic):

        #Shows dictionary of the current directory's dictionary.

        listofdic,atss = self.openfile(dic)
        
        for line in listofdic:
            
            item = QtWidgets.QListWidgetItem()
            
            line = line.replace("\n","")
            line = line.replace(" '{","'{")
            item.setText(str(line))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
            self.listWidget.addItem(item)
            #print(line)

    def change(self,item):
        print("clicked"+item.text()+ " DF Line 472")
        t = item.text()
        item.setText("")
        
    def openfile(self,dir):

        #Takes a directory and returns a dictionary in the text file.

        st = ""
        with open(dir) as f:
            text = f.readlines()
        for i in text:
            st += i
        
        tdict = st
        
        return text,tdict

    def addopenfunc(self):
        
        #Creates an addWindow object, and checks mutual data for its current color and arabic settings.
        # Also connects all the major functions to its buttons and lastly shows the window. 

        global addWindow
        addWindow = QtWidgets.QMainWindow()
        addui = Ui_addWindow()
        addui.setupUi(addWindow)

        addWindow.hide()

        addWindow.setWindowIcon(QtGui.QIcon(
            ':icons\\icons\\ankh_icon.png'))
        
        if mutualData.btncolors == "d":
            self.changecolordark(addui)
        elif mutualData.btncolors == "w":
            self.changecolorlight(addui)
        
        if mutualData.defaultLanguage == "English":
            self.changeLangEn(addui)
        elif mutualData.defaultLanguage == "Arabic":
            self.changeLangAr(addui)
            

        addui.addBtnSing.clicked.connect(lambda: (self.addBtnSingleMeaning(self.atss,addui)))
        addui.cancelBtnSing.clicked.connect(lambda: (addWindow.close()))
        addui.addBtnListMulti.clicked.connect(lambda: (self.addMeaning(addui)))
        addui.removeBtnListMulti.clicked.connect(lambda: (self.removeMeaning(addui)))
        addui.addBtnMulti.clicked.connect(lambda: (self.addBtnMultiMeaning(self.atss,addui)))
        addui.cancelBtnMulti.clicked.connect(lambda: (addWindow.close()))
        
        

        addWindow.show()

    def addMeaning(self,addui):

        #Add meaning function for adding a word with multiple meanings, it adds items to the list widget (for meanings.).

        item = QtWidgets.QListWidgetItem()
        item.setText("-")
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        addui.transListMulti.addItem(item)

    def removeMeaning(self,addui):

        #Removes meanings from the list widget of the add word with mutltiple meanings.

        selectedItem = addui.transListMulti.selectedItems()
        if not selectedItem:
            return        
        for item in selectedItem:
            bruh =item.text() 
            print(bruh+ " DF Line 543")
            addui.transListMulti.takeItem(addui.transListMulti.row(item))

    def addBtnMultiMeaning(self,atss,addui):

        #Function for the add button, it takes the dictionary to save it to, and the add object.
        # It takes the info from the text edits and saves them to the dictionary. And for the multiple meanings, 
        # it takes the items inside the list widget and adds them one by one to the word. 
        # If something is empty, it returns an error message in the status label. 

        if len(self.tempdictforsave) == 0:
            new = ast.literal_eval(atss)
        elif len(self.tempdictforsave) != 0:
            new = ast.literal_eval(self.st)

        items = []
        for x in range(addui.transListMulti.count()):
            items.append(addui.transListMulti.item(x).text())

        g = addui.gardTextEditMulti.toPlainText()
        tl = addui.translTextEditMulti.toPlainText()
        t = addui.transListMulti.count()

        gw = "{" + g + "}"
        
        if (g != "" and tl != "" and t != 0):
            if  gw not in new:
                transl = "[" + addui.translTextEditMulti.toPlainText() + "] "
                trans = []
                for i in items:
                    newtrans = transl + " " + i
                    trans.append(newtrans)

                gard = "{" + addui.gardTextEditMulti.toPlainText() + "}"
                #print(gard + ": "+ comb)
                new[gard] = trans



                addui.statusLabel.setText("Added successfully")
                addui.statusLabel.setStyleSheet("color:rgb(55,255,55)")
                addui.gardTextEditMulti.setPlainText("")
                addui.translTextEditMulti.setPlainText("")
                addui.transListMulti.clear()
                print(str(items)+ " DF Line 587")
                self.changeStatusIconPending()



                self.tempdictforsave.clear()
                tdictsave = str(new)
                tdictsave = tdictsave.replace(", '{",",\n '{")
                for i in tdictsave.split("\n"):
                    self.tempdictforsave.append(i)
                self.st = ""
                for i in self.tempdictforsave:
                    self.st += i
                self.showupdateddic(self.tempdictforsave)

                mainFunctions.saveLog(("Added a word with multiple meanings with key: " + gard + "."))
                
                


            else:
                addui.statusLabel.setText("Key already exists.")
                addui.statusLabel.setStyleSheet("color:rgb(55,55,255)")

        else:
            addui.statusLabel.setText("Please fill all the fields.")
            addui.statusLabel.setStyleSheet("color:rgb(255,55,55)")


        self.timer.start(5000)
        self.timer.timeout.connect(lambda: self.timeoutForAdd(addui))

    def useaddui(self):

        #Makes an object of addWindow for usage.

        global addWindow
        addWindow = QtWidgets.QMainWindow()
        addui = Ui_addWindow()
        addui.setupUi(addWindow)
        
    def changecolordark(self,addui):

        #Changes the colors of the add window to dark theme using stylesheets.
        
        addui.addBtnListMulti.setStyleSheet("QPushButton {color: #333;\n"
            "border: 2px solid rgba(29, 55, 74,100%);\n"
            "border-radius: 10px;\n"
            "background: rgba(75, 75, 75,95%);\n"
            "color: rgb(200, 200, 200);}\n"
            "QPushButton:hover {\n"
            "background: rgb(40, 40, 40);}\n"
            "QPushButton:pressed {\n"
            "border-style: inset;\n"
            "background: rgb(55, 55, 55);}\n") 
        addui.addBtnMulti.setStyleSheet("QPushButton {color: #333;\n"
        "border: 2px solid rgba(29, 55, 74,100%);\n"
        "border-radius: 10px;\n"
        "background: rgba(75, 75, 75,95%);\n"
        "color: rgb(200, 200, 200);}\n"
        "QPushButton:hover {\n"
        "background: rgb(40, 40, 40);}\n"
        "QPushButton:pressed {\n"
        "border-style: inset;\n"
        "background: rgb(55, 55, 55);}\n") 
        addui.addBtnSing.setStyleSheet("QPushButton {color: #333;\n"
        "border: 2px solid rgba(29, 55, 74,100%);\n"
        "border-radius: 10px;\n"
        "background: rgba(75, 75, 75,95%);\n"
        "color: rgb(200, 200, 200);}\n"
        "QPushButton:hover {\n"
        "background: rgb(40, 40, 40);}\n"
        "QPushButton:pressed {\n"
        "border-style: inset;\n"
        "background: rgb(55, 55, 55);}\n") 
        addui.cancelBtnMulti.setStyleSheet("QPushButton {color: #333;\n"
        "border: 2px solid rgba(29, 55, 74,100%);\n"
        "border-radius: 10px;\n"
        "background: rgba(75, 75, 75,95%);\n"
        "color: rgb(200, 200, 200);}\n"
        "QPushButton:hover {\n"
        "background: rgb(40, 40, 40);}\n"
        "QPushButton:pressed {\n"
        "border-style: inset;\n"
        "background: rgb(55, 55, 55);}\n") 
        addui.cancelBtnSing.setStyleSheet("QPushButton {color: #333;\n"
        "border: 2px solid rgba(29, 55, 74,100%);\n"
        "border-radius: 10px;\n"
        "background: rgba(75, 75, 75,95%);\n"
        "color: rgb(200, 200, 200);}\n"
        "QPushButton:hover {\n"
        "background: rgb(40, 40, 40);}\n"
        "QPushButton:pressed {\n"
        "border-style: inset;\n"
        "background: rgb(55, 55, 55);}\n") 
        addui.removeBtnListMulti.setStyleSheet("QPushButton {color: #333;\n"
        "border: 2px solid rgba(29, 55, 74,100%);\n"
        "border-radius: 10px;\n"
        "background: rgba(75, 75, 75,95%);\n"
        "color: rgb(200, 200, 200);}\n"
        "QPushButton:hover {\n"
        "background: rgb(40, 40, 40);}\n"
        "QPushButton:pressed {\n"
        "border-style: inset;\n"
        "background: rgb(55, 55, 55);}\n") 

        addui.gardLabelMulti.setStyleSheet("color: rgb(200,200,200)")
        addui.gardLabelSing.setStyleSheet("color: rgb(200,200,200)")
        addui.statusLabel.setStyleSheet("color: rgb(255,255,255)")
        addui.transLabelMulti.setStyleSheet("color: rgb(200,200,200)")
        addui.TransLabelSing.setStyleSheet("color: rgb(200,200,200)")
        addui.translLabelMulti.setStyleSheet("color: rgb(200,200,200)")
        addui.translLabelSing.setStyleSheet("color: rgb(200,200,200)")
        

        addui.lineLabelMulti.setStyleSheet("background-color: rgb(0, 0, 0);")
        addui.lineLabelSing.setStyleSheet("background-color: rgb(0, 0, 0);")
        addui.midLine.setStyleSheet("""Line {background-color: rgb(0, 0, 0);
margin: 12px 0px 12px 0px;}""")

        addui.mainBackgroundLabel.setStyleSheet("border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmalldark.png);")
        addui.multiMainLabel.setStyleSheet("color: rgb(200,200,200)")
        addui.singMainLabel.setStyleSheet("color: rgb(200,200,200)")

        
        addui.gardTextEditMulti.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
            "color: rgb(200, 200, 200);\n"
            "border: 2px;\n"
            "border-style: solid;\n"
            "border-color: rgba(29, 55, 74,100%);\n")
        addui.gardTextEditSing.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
            "color: rgb(200, 200, 200);\n"
            "border: 2px;\n"
            "border-style: solid;\n"
            "border-color: rgba(29, 55, 74,100%);\n")
        addui.translTextEditMulti.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
            "color: rgb(200, 200, 200);\n"
            "border: 2px;\n"
            "border-style: solid;\n"
            "border-color: rgba(29, 55, 74,100%);\n")
        addui.translTextEditSing.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
            "color: rgb(200, 200, 200);\n"
            "border: 2px;\n"
            "border-style: solid;\n"
            "border-color: rgba(29, 55, 74,100%);\n")
        addui.transTextEditSing.setStyleSheet("background-color:rgba(0, 0, 0,50%);\n"
            "color: rgb(200, 200, 200);\n"
            "border: 2px;\n"
            "border-style: solid;\n"
            "border-color: rgba(29, 55, 74,100%);\n")
        addui.transListMulti.setStyleSheet("QListWidget{\n"
"background-color: rgba(0, 0, 0,50%);\n"
"color: rgb(200, 200, 200);\n"
"border: 2px;\n"
"border-style: solid;\n"
"border-color: rgba(29, 55, 74,100%);}"

"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        
    def changecolorlight(self,addui):

        #Changes the colors of the add window to light theme using stylesheets.

        addui.addBtnListMulti.setStyleSheet("QPushButton {\n"
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
        addui.addBtnMulti.setStyleSheet("QPushButton {\n"
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
        addui.addBtnSing.setStyleSheet("QPushButton {\n"
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
        addui.cancelBtnMulti.setStyleSheet("QPushButton {\n"
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
        addui.cancelBtnSing.setStyleSheet("QPushButton {\n"
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
        addui.removeBtnListMulti.setStyleSheet("QPushButton {\n"
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

        addui.gardLabelMulti.setStyleSheet("color: rbg(200,200,200)")
        addui.gardLabelSing.setStyleSheet("color: rbg(200,200,200)")
        addui.statusLabel.setStyleSheet("color: rgb(105, 105, 157)")
        addui.transLabelMulti.setStyleSheet("color: rbg(200,200,200)")
        addui.TransLabelSing.setStyleSheet("color: rbg(200,200,200)")
        addui.translLabelMulti.setStyleSheet("color: rbg(200,200,200)")
        addui.translLabelSing.setStyleSheet("color: rbg(200,200,200)")
        

        addui.lineLabelMulti.setStyleSheet("color: rbg(200,200,200)")
        addui.lineLabelSing.setStyleSheet("color: rbg(200,200,200)")


        addui.mainBackgroundLabel.setStyleSheet("border-image: url(:/icons/icons/118Z_2012.w026.n002.13B.p1.13 blurredsmall.png);")
        addui.multiMainLabel.setStyleSheet("color: rbg(200,200,200)")
        addui.singMainLabel.setStyleSheet("color: rbg(200,200,200)")

        
        addui.gardTextEditMulti.setStyleSheet("""background-color: rgba(255, 255, 255,95);
border: 2px;
border-style: solid;
border-color: rgb(105, 105, 157);
""")
        addui.gardTextEditSing.setStyleSheet("""background-color: rgba(255, 255, 255,95);
border: 2px;
border-style: solid;
border-color: rgb(105, 105, 157);
""")
        addui.translTextEditMulti.setStyleSheet("""background-color: rgba(255, 255, 255,95);
border: 2px;
border-style: solid;
border-color: rgb(105, 105, 157);
""")
        addui.translTextEditSing.setStyleSheet("""background-color: rgba(255, 255, 255,95);
border: 2px;
border-style: solid;
border-color: rgb(105, 105, 157);
""")
        addui.transTextEditSing.setStyleSheet("""background-color: rgba(255, 255, 255,95);
border: 2px;
border-style: solid;
border-color: rgb(105, 105, 157);
""")
        addui.transListMulti.setStyleSheet("""background-color: rgba(255, 255, 255,95);
border: 2px;
border-style: solid;
border-color: rgb(105, 105, 157);
""")

    def changeLangEn(self,addui):

        #Changes language for the addWindow to english.

        addWindow.setWindowTitle("Add words")
        addui.gardLabelSing.setText("Gardiners code")
        addui.translLabelSing.setText("Transliteration")
        addui.TransLabelSing.setText("Translation")
        addui.singMainLabel.setText("Add a word with a single meaning.")
        addui.addBtnSing.setText("Add")
        addui.cancelBtnSing.setText("Cancel")
        addui.translLabelMulti.setText("Transliteration")
        addui.cancelBtnMulti.setText("Cancel")
        addui.gardLabelMulti.setText("Gardiners code")
        addui.transLabelMulti.setText("Translation")
        addui.addBtnMulti.setText("Add")
        addui.addBtnListMulti.setText("Add")
        addui.removeBtnListMulti.setText("Remove")
        addui.multiMainLabel.setText("Add a word with multiple meanings.")
        addui.statusLabel.setText("------------------------------------------------------")

    def changeLangAr(self,addui):

        #Changes language of the addWindow to arabic.

        addWindow.setWindowTitle("أضف كلمات")
        addui.gardLabelSing.setText("كود غاردينر")
        addui.translLabelSing.setText("الترجمة الحرفية")
        addui.TransLabelSing.setText("ترجمة")
        addui.singMainLabel.setText("أضف كلمة ذات معنى واحد.")
        addui.addBtnSing.setText("أضف")
        addui.cancelBtnSing.setText("الغاء")
        addui.translLabelMulti.setText("الترجمة الحرفية")
        addui.cancelBtnMulti.setText("الغاء")
        addui.gardLabelMulti.setText("كود غاردينر")
        addui.transLabelMulti.setText("ترجمة")
        addui.addBtnMulti.setText("أضف")
        addui.addBtnListMulti.setText("أضف")
        addui.removeBtnListMulti.setText("ازالة")
        addui.multiMainLabel.setText("أضف كلمة متعددة المعاني.")
        addui.statusLabel.setText("------------------------------------------------------")

    





""" app = QtWidgets.QApplication(sys.argv)
myWindow = dictionaryFunctions()
myWindow.show()
app.exec_() """