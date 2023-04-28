import mainFunctions
import os
from PyQt5.QtCore import QTimer


class mutualData():

    #Records data to be used between the main GUI and the dictionary class.

    directoryname = "dictionaries\\defaultDictionary.txt"
    filename = os.path.basename(directoryname)
    currentdictionary = mainFunctions.useDir(directoryname)
    #print(directoryname + " MD Line 13")

    defaultdic = ""

    darkmodestat = False
    boldtextstat = False
    showdatestat = False
    showtimestat = False

    defaultLanguage = "English"

    btncolors = "w"
    boldcheck = False

    dictionaryForSettings = {}

    previoussaved = ""

    combo1 = 0
    combo2 = 0


