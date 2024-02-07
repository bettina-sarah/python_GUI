from tkinter import *

# librairie de widget
# AUTRE FACON DE IMPORT: import tkinter as tk  # tu dit tk.button ...

#interface graphique minimale - window
# grosseur moniteur, pixel, color etc... special function: Tk() assigné a la var root

class Vue():
    def __init__(self, parent):
        self.parent = parent
        self.root = Tk()  # comme dans linux, . = root
        mavar = Label(self.root, text="bienvenue au cours de C31-intensif")
        mavar.pack()
        mavar2 = Button(self.root, text="Cours graphique", command=self.afficher_bienvenue)
        mavar2.pack()

    def afficher_bienvenue(self):
        print("bienvenue encore (button)")


# pas besoin de dire tkinter.button ... tkinter etc
# os cree une nouvelle espace de nom (namespace) qui est pas main (mettons len comme nom fonc si on veut)
# label (parent,
# dans param sans espaces
# GESTIONNAIRE DE GEOMETRIE - pour attacher au root - le visualiser
# 1. Pack (package) - comme wrap_content en java
# 2. Grid (avec des attributs - column & row (grille de placement)
# 3. Place (en % aussi - devient dynamique .. grandit 10% etc)
# !! un seul gestionnaire par widget
# widget frame fait pour regrouper des choses ... mais a l'interieur, on peut mettre grid OU pack
# chaque frame avec son propre gestionnaire de geometrie

# !!! command = func sans () pour que la fonc s'execute seulement qunad le button est pressed

class Modele():
    def __init__(self, parent):
        self.parent = parent

class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self)
        self.vue.root.mainloop()





