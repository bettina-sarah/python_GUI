from tkinter import *


class Vue():
    def __init__(self, parent):
        self.root = Tk()  # comme dans linux, . = root
        mavar = Label(self.root, text="bienvenue au cours de C31-intensif")
        mavar.pack()
        mavar2 = Button(self.root, text="Cours graphique", command=self.afficher_bienvenue)
        mavar2.pack()
        # pack_forget (loading...)

    # fonc avec self tjrs en param dans un objet !!!
    def afficher_bienvenue(self):
        print("bienvenue encore (button)")


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 500
        self.hauteur = 500


class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self)
        self.vue.root.mainloop()


if __name__ == "__main__":
    c = Controleur()
    # sans () objet mais execute pas tt de suite
