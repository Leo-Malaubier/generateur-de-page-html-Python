from tkinter import *
import connexionClass
import UserPage
class MainClass(Tk): #InitFrame érite de toutes les méthodes de la classe tk
    def __init__(self):
        Tk.__init__(self) # nouvelle instante de Tk
        self.MaFrame = None #commance par définir une variable frame qui permet de définir s'il y a une frame ou pas, si oui on la supprime pour en re faire une autre
        self.switch(connexionClass.Connexion)

    def switch(self, frame):
        #destruction de la frame actuelle
        NouvelleFrame = frame(self)
        if self.MaFrame is not None: #=> ducoup si MaFrame n'erst pas vide paff on la supprime
            self.MaFrame.destroy()
        self.MaFrame = NouvelleFrame
        try:
            if NouvelleFrame.NomCLASS =="salut": #On veux savoir de quelle frame on parle donc ducoup on a une variable de vérification par class
                print("aie")
            if NouvelleFrame.NomCLASS =="Connexion":
                self.MaFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
                
            if NouvelleFrame.NomCLASS =="UserPage":
                self.MaFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        except:
            pass


if __name__ == "__main__":
    windows = MainClass()
    windows.title('Projet')
    windows.geometry("800x600")
    windows.minsize(500,400)
    windows.maxsize(800,600)
    windows.config(background="#FFCE30")

    windows.mainloop()
