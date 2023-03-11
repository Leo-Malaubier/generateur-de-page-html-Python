from tkinter import *
import UserPage
import login
import main
#import Selection

class Connexion(Frame):
    NomCLASS= "Connexion"
    def __init__(self, pere):


        self.Connexion=False
        self.Utilisateur= ""

        self.Id = StringVar()
        self.MDP = StringVar()

        Frame.__init__(self, pere)

        self.pere=pere
        label1 = Label(self,text = "identifiant")#mise en place de l'interface
        label1.grid(column=0, row=0, ipadx=5, pady=5)

        label2 = Label(self,text = "mot de passe")
        label2.grid(column=0, row=1, ipadx=5, pady=5)


        self.Entre1 = Entry(self, width=20,textvariable=self.Id,show='*')
        #self.Entre1.focus_set()
        self.Entre2 = Entry(self, width=20,textvariable=self.MDP,show='*')
        #self.Entre2.focus_set()

        self.Entre1.grid(column=1, row=0, padx=10, pady=5)
        self.Entre2.grid(column=1, row=1, padx=10, pady=5)


        resultButton = Button(self, text = 'connexion',command=self.testLogin)
        resultButton.grid(column=0, row=2, pady=10)

        #supButton = Button(self.fra, text = 'sup',command=self.dest)
        #supButton.grid(column=1, row=2, pady=10)


    def testLogin(self): #connexion avec affichage des erreur
        Var,Users=login.Liaison(self.Entre1.get(),self.Entre2.get())
        print(Var)
        try:  #supprime les encienes erreur (permet de pas avoir de superposition a l'affichage)
            self.labelErr.destroy()
        except:
            pass

        if Var==True:
            if Users=="SimpleUsers":
                self.Utilisateur="SimpleUsers"
                self.pere.switch(UserPage.UserPage)
            else:
                self.Utilisateur="SuperUtilisateur"


        elif Var == "Faux":
            self.labelErr=Label(self, text="erreur de connexion essayé un autre mot de passe ou identifiant")
            self.labelErr.grid(column=3, row=0, ipadx=5, pady=5)

        elif Var== 'Rien':
            self.labelErr=Label(self, text="Aucun mots de passe ou identifiant")
            self.labelErr.grid(column=3, row=0, ipadx=5, pady=5)

"""
    def creation(self):
        Selection.UserPage(self.fra,self.fra2)
"""
