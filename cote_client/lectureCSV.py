import os #permet de géré des fichier
import pandas as pd
import numpy as np
def ListeFichiercsv(): #liste de nom des fichier csv
        list =(os.listdir('temps/xlsxTOcsvTemp/'))
        MALISTE=[]
        for i in range(len(list)):
            try:
                if list[i].split('.')[1]=='csv':
                    MALISTE.append(list[i])
            except:
                pass
        return MALISTE
def ListeFichierxlsx(emplacement): #liste de nom des fichier csv
        list =(os.listdir(emplacement))
        MALISTE=[]
        for i in range(len(list)):
            try:
                if list[i].split('.')[1]=='xlsx':
                    MALISTE.append(list[i])
            except:
                pass
        return MALISTE

def Fichierxlsx():
    list=(os.listdir('temps/'))
    for i in range(len(list)):
        if list[i].split('.')[1]=='xlsx':
            return list[i]

def Rubrique():
    MonFichier=Fichierxlsx()
    xls = pd.ExcelFile('temps/'+MonFichier)#Objet type ExcelFile
    for i in range(len(xls.sheet_names)):
        if xls.sheet_names[i]=='Rubrique':
            data = pd.read_excel('temps/'+MonFichier, sheet_name=xls.sheet_names[i], usecols="A")
            data=data.dropna(axis=0)
            data=data.to_numpy()

    return data

def lecture_fueilles():
    data=[]
    MonFichier=Fichierxlsx()
    xls = pd.ExcelFile('temps/'+MonFichier)#Objet type ExcelFile
    for i in range(len(xls.sheet_names)):
        temps=None
        temps=pd.read_excel('temps/'+MonFichier, sheet_name=xls.sheet_names[i], usecols="A:E")
        Np=temps.to_numpy()
        data.append([xls.sheet_names[i],Np])

    return data

"""
#Pour que cela fonction, on a: [][][][] 4 élément différent. le premier correspond a la feuille, le second ne peux être que 1 ou 0
#s'il est de 0 on ne peux pas mettre de suite, cela n'affichera rien. il correspond au nom de la fueille.
#quand le second élément est a 1, alor on peux rajouté 2 autre option qui permette d'axédé au information de la feuille.
#on peux accédé a une ligne en particulier(du tableau xlsx), et si l'on met le dernier [] on axède a une case précisément
représentation: [[element,[[],[],[]]],[element,[[],[],[]]],[element,[[],[],[]]]]
"""
