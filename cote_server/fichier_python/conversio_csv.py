from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox #permet de faire des message d'alert
#installer le module pandas et openpyxl
import pandas as pd #lire les fichier excel
import shutil #permet de copier un fichier
import os #permet de géré des fichier


class Conversion:
    def __init__(self,date):
        #permet d'ouvrir le fichier d'on on a le lien en fait une copie et transforme cette copie en csv
        destination='../fichier_csv/'+date
        #print(self.NomSimple)
        if not os.path.exists('../fichier_csv/'+date):
            os.makedirs('../fichier_csv/'+date)
        self.ListeFichierxlsx()

        for i in range(len(self.MALISTE)):
            read_file = pd.read_excel('../fichier_temporaires/'+self.MALISTE[i]+'.xlsx')
            read_file.to_csv('../fichier_temporaires/'+self.MALISTE[i]+'.csv',index=None,header=True)
            shutil.move('../fichier_temporaires/'+self.MALISTE[i]+'.csv', destination)



    def ListeFichierxlsx(self): #liste de nom des fichier csv
            list =(os.listdir('../fichier_temporaires/'))
            self.MALISTE=[]
            for i in range(len(list)):
                if list[i].split('.')[1]=='xlsx':
                    self.MALISTE.append(list[i].split('.')[0])
#Conversion("Juin 2000")

    def suppression(self):
        shutil.rmtree('../fichier_temporaires')
        if not os.path.exists('../fichier_temporaires'):
            os.makedirs('../fichier_temporaires')
