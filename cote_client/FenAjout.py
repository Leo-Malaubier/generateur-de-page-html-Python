from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox #permet de faire des message d'alert
#installer le module pandas et openpyxl
import pandas as pd #lire les fichier excel
import shutil #permet de copier un fichier
import os #permet de géré des fichier
import datetime
import suppression

class Recherche:

    def __init__(self):
        self.Recherche()

    def Recherche(self):
        suppression.main()
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.xlsx*"),("all files","*.*")))
        self.f= filename  #nom du fichier

        self.ConvertXlsxToCsv()

    def ConvertXlsxToCsv(self): #permet d'ouvrir le fichier d'on on a le lien en fait une copie et transforme cette copie en csv
        source=self.f
        self.NomSimple=source.split('/')[-1]
        destination='temps/'+self.NomSimple
        #print(self.NomSimple)
        shutil.copyfile(source, destination)
