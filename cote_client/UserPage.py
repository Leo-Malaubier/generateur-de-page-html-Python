from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox #permet de faire des message d'alert
#installer le module pandas et openpyxl
import pandas as pd
import shutil #permet de copier un fichier
import os #permet de géré des fichier
import FenAjout
import lectureCSV

class UserPage(Frame):
    NomCLASS= "UserPage"
    def __init__(self, pere):
        Frame.__init__(self, pere)

        tab_frame = Frame(self)
        tab_frame.pack()

        #Scrollbar
        #y
        self.scroll = Scrollbar(tab_frame)
        self.scroll.pack(side=RIGHT, fill=Y)

        #x
        self.scrollx = Scrollbar(tab_frame,orient='horizontal')
        self.scrollx.pack(side= BOTTOM,fill=X)

        #Treeview

        self.tab= ttk.Treeview(tab_frame,yscrollcommand=self.scroll.set, xscrollcommand =self.scrollx.set,selectmode='browse')
        self.tab.pack()

        self.scroll.config(command=self.tab.yview)
        self.scrollx.config(command=self.tab.xview)
        #vsb.place(x=30+200+2, y=95, height=200+20)
        self.tab['columns']= ('Date','Rubrique','Titre','Description ou lien','lien facultatif')

        for i in self.tab['columns']:
            self.tab.column(i,anchor=CENTER,width=90,stretch=NO)
            self.tab.heading(i,text=i,anchor=CENTER)
        self.tab.heading("#0",text="Envoie",anchor=CENTER)
        self.tab.column("#0", width=80,  stretch=NO)



        self.Input_frame = Frame(self)
        self.Input_frame.pack()



        LabDate= Label(self.Input_frame,text="Date")
        LabDate.grid(row=0,column=1)

        LabRubrique = Label(self.Input_frame,text="Rubrique")
        LabRubrique.grid(row=0,column=2)

        LabTitre= Label(self.Input_frame,text="Titre")
        LabTitre.grid(row=2,column=0)

        LabResume = Label(self.Input_frame,text="Résumé")
        LabResume.grid(row=2,column=1)

        LabLien= Label(self.Input_frame,text="Lien(facultatif)")
        LabLien.grid(row=2,column=2)

        self.date_entre = Entry(self.Input_frame)
        self.date_entre.grid(row=1,column=1)

        self.Rubi_entre= Entry(self.Input_frame)
        self.Rubi_entre.grid(row=1,column=2)

        self.titre_entre= Entry(self.Input_frame)
        self.titre_entre.grid(row=3,column=0)

        self.resume_entre= Entry(self.Input_frame)
        self.resume_entre.grid(row=3,column=1)

        self.lien_entre= Entry(self.Input_frame)
        self.lien_entre.grid(row=3,column=2)
        #button
        """
        select_button = Button(self.Input_frame,text="Select Envoie", command=self.select_envoie)
        select_button.grid(row=4,column=0)
        """
        Input_button = Button(self.Input_frame,text = "Ajouter",command=self.ajoute)
        Input_button.grid(row=4,column=1)

        edit_button = Button(self.Input_frame,text="Modifier ",command=self.modifier)
        edit_button.grid(row=4,column=2)

        button_exit = Button(self.Input_frame,text = "quitter",command = exit)
        button_exit.grid(row=5,column=0)

        button_Add = Button(self.Input_frame,text = "Ajouter un fichier xlsx",command = lambda:FenAjout.Recherche())
        button_Add.grid(row=5,column=1)

        button_Actualise = Button(self.Input_frame,text = "Actualiser",command =self.affichage)
        button_Actualise.grid(row=5,column=2)

        button_Envoyer = Button(self.Input_frame,text = "Envoyer",command =self.ecriture)
        button_Envoyer.grid(row=5,column=3)
    def affichage(self):
        enssemble=lectureCSV.lecture_fueilles()
        self.data_parent=[]
        self.data=[]
        for n in range(len(enssemble)):
            if n==0:
                pass
            else:
                self.data_parent.append(enssemble[n][0])
                autre=[]
                for i in range(len(enssemble[n][1])): #8
                    salut=[]
                    for k in range(len(enssemble[n][1][i])): #5
                        salut.append(enssemble[n][1][i][k])
                    autre.append(salut)
                self.data.append(autre)
        #print(self.data)
        #forme de la data= [[[],[],[]],[[],[],[]]]
        for i in range(len(self.data_parent)):
                self.tab.insert(parent='',index=i,iid=i+1,text=self.data_parent[i]) #/!\ bien il faut que l'iid soit différente de 0 car l'iid de 0 est la liste de tout les parent, il y a un conflit s'il y a 2 iid=0
                self.count=i

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                value=self.data[i][j]
                self.tab.insert(parent=i+1,index='end',text='',values=value)


    def ajoute(self):

        try:
            selected=self.tab.focus()
            valeur=int(selected)
            valeur+=1
        except:
            messagebox.showerror("Attention", "Vous devez sélectionné un nom d'équipe")

        if(self.date_entre.get() and self.Rubi_entre.get() and self.titre_entre.get() and self.resume_entre.get()) == "":
            #print("vous devez remplire les champ")
            messagebox.showwarning("Attention", "Veiller à bien remplire tous les paramètre indispensable:  \n -Feuille\n -Date\n -Rubrique\n -Équipe\n -Titre\n -Résumé")
        else:
            self.tab.insert(parent=self.tab.index(valeur),index='end',text="",values=(self.date_entre.get(),self.Rubi_entre.get(),self.titre_entre.get(),self.resume_entre.get(),self.lien_entre.get()))

            self.date_entre.delete(0,END)
            self.Rubi_entre.delete(0,END)
            #self.equipe_entre.delete(0,END)
            self.titre_entre.delete(0,END)
            self.resume_entre.delete(0,END)
            self.lien_entre.delete(0,END)

    def modifier(self):
        selected=self.tab.focus()
        if self.tab.item(selected)["text"] not in self.data_parent:
            self.tab.item(selected,text="",values=(self.date_entre.get(),self.Rubi_entre.get(),self.titre_entre.get(),self.resume_entre.get(),self.lien_entre.get()))
            #clear entry boxes
            self.date_entre.delete(0,END)
            self.Rubi_entre.delete(0,END)
            #self.equipe_entre.delete(0,END)
            self.titre_entre.delete(0,END)
            self.resume_entre.delete(0,END)
            self.lien_entre.delete(0,END)

    def select_envoie(self):
        #grab record
        selected=self.tab.focus()
        #grab record values
        if self.tab.item(selected)["text"] == "envoie":
            self.tab.item(selected,text="")
        elif self.tab.item(selected)["text"]=="":
            self.tab.item(selected,text="envoie")
        else:
            pass


    def verif(self):#vérifie la liste d'envoie (pour le moment elle vérifie que seul des élément a l'intérieur des rubriques sont sélectionné, et interdit tout sélection de rubrique)
        try:
            if len(self.IdListeEnvoie)>0:
                del self.IdListeEnvoie[0:len(self.IdListeEnvoie)]
        except:
            self.IdListeEnvoie=[]

        for i in range(len(self.data_parent)):
            liste_enfants=self.tab.get_children(i+1)
            for j in liste_enfants:
                #print(j)
                if self.tab.item(j)["text"]=="envoie":
                        self.IdListeEnvoie.append(j)
    """
    def ecriture(self):
        for i in range(len(self.data_parent)):
            test=self.tab.get_children(i+1)
            count=0
            parent=self.data_parent[i]
            writer = pd.ExcelWriter("temps/xlsxTOcsvTemp/"+parent+'.xlsx')
            for j in range(len(test)):
                if j!=0:
                    count+=6
                else:
                    count=0
                valeur=self.tab.item(test[j])
                print(valeur["values"])
                df1 = pd.DataFrame({'Data': valeur["values"]})
                df1.to_excel(writer, sheet_name ='Sheet1',startrow=count)
            writer.save()
            """
    #version temporaire
    def ecriture(self):
        for i in range(len(self.data_parent)):
            test=self.tab.get_children(i+1)
            count=0
            parent=self.data_parent[i]
            writer = pd.ExcelWriter("../cote_server/fichier_temporaires/"+parent+'.xlsx')
            for j in range(len(test)):
                if j!=0:
                    count+=6
                else:
                    count=0
                valeur=self.tab.item(test[j])
                print(valeur["values"])
                df1 = pd.DataFrame({'Data': valeur["values"]})
                df1.to_excel(writer, sheet_name ='Sheet1',startrow=count)
            writer.save()
