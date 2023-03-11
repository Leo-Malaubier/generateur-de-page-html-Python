
import os #permet de géré des fichier
import pandas as pd

def liste_fichier():
    list =(os.listdir('../fichier_temporaires/'))
    MALISTE=[]
    for i in range(len(list)):
        if list[i].split('.')[1]=='xlsx':
            MALISTE.append(list[i].split('.')[0])
    return MALISTE

def lecture_fueilles():
    MALISTE=liste_fichier()
    data=[]
    for i in range(len(MALISTE)):
        if MALISTE[i]=='Rubrique':
            pass
        else:
            temps=None
            temps=pd.read_excel('../fichier_temporaires/'+MALISTE[i]+'.xlsx', sheet_name=0, usecols="B")
            Np=temps.to_numpy()
            data.append([Np])
    return data

def lecture_data():
    MALISTE=liste_fichier()
    MALISTE.remove('Rubrique')
    data=lecture_fueilles()
    NewListe=[]
    for i in range(len(data)):
        if len(data[i][0]) >0:
            NewListe.append(MALISTE[i])
        for j in range(len(data[i][0])):
            if data[i][0][j][0]=='Data':
                data[i][0][j][0]=MALISTE[i]
            NewListe.append(data[i][0][j][0])
    return NewListe


def rangement():
    data=lecture_data()
    ListePrincipal=[]
    Nb=len(data)
    Nb=Nb/6
    Nb=int(Nb)
    for i in range(Nb):
        NewListe=[]
        for j in range(6):
            variable=data.pop(0)
            NewListe.append(variable)
        ListePrincipal.append(NewListe)
    return ListePrincipal


"""
ici la structure est en 3 temps [][][][]
[premier liste][tout les élément de la liuste][chaque case de la liste][contenue de chaque cases]
"""
