
import os #permet de géré des fichier
import pandas as pd
import numpy as np


def lecture_fueilles():
    data=[]
    temps=pd.read_excel('../fichier_temporaires/Rubrique.xlsx', sheet_name=0, usecols="B")
    Np=temps.to_numpy()
    data.append([Np])
    NewListe=[]
    NewListe.append(data[0][0][0][0])
    t=type(data[0][0][0][0])
    #j'ai remarqué la la valeur 'nan' de la liste Rubrique, a pour type float, on ne peux donc pas faire de vérification if data[nan] == 'nan' vu que l'on fait if float == string
    #on compare donc simplement les type des variables
    for i in range(len(data[0][0])):
        if data[0][0][i][0]=='Data':
            if type(data[0][0][i+1][0])==t:
                NewListe.append(data[0][0][i+1][0])
        if i==len(data[0][0])-1:
            return NewListe
