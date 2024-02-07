import random
from tkinter import *

class Vue():
    def __init__(self, parent, modele):
        self.root = Tk()  # comme dans linux, . = root
        self.parent = parent
        self.modele = modele
        mavar = Label(self.root, text="bienvenue au cours de C31-intensif")
        mavar.pack()
        mavar2 = Button(self.root, text="Cours graphique", command=self.creer_pion_vue)
        mavar2.pack()
        # pack_forget (loading...)
        #canvas class: needs params: root, w, h, bg(background)
        self.canvas = Canvas(self.root, width=self.modele.largeur, height=self.modele.hauteur, bg="medium slate blue")
        self.canvas.bind("<Button>", self.get_position) # bouton SOURIS !
        self.canvas.pack()

    def get_position(self, evt):
        # bind lié canvas au evenenemtn du bouton souris...
        # canvas find withtag: trouve element ou on click avec le tag "current" (python donne au chose qui est en sous du souris)
        chose = self.canvas.find_withtag("current")
        if chose:
            print(chose, evt.x, evt.y)

    # fonc avec self tjrs en param dans un objet !!!
    def creer_pion_vue(self):
        self.parent.creer_pion_controleur()
    def afficher_pions(self):
        # chaque button, pion se crée, pi on redessine tt a chaque button, on efface les vieux
        # delete au depart
        self.canvas.delete("all")
        for i in self.modele.pions:
            # creer rectangle: 2 paire de points - 1ere, xy, 2eme: x+taille, y+taille

            self.canvas.create_rectangle(i.posX, i.posY,
                                         i.posX+i.taille, i.posY+i.taille, fill="DeepPink2")



class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 500
        self.hauteur = 500
        self.pions = []

    def creer_pion_modele(self):
        x = random.randrange(self.largeur)
        y = random.randrange(self.hauteur)
        p = Pion(self, x, y)
        self.pions.append(p)


class Pion():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.taille = 30
        self.posX = x
        self.posY = y
        #none pcq on demane au parent de les creer (modele)

class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.vue.root.mainloop()

    def creer_pion_controleur(self):
        self.modele.creer_pion_modele()
        self.vue.afficher_pions()
        print("nbr pions:", len(self.modele.pions))


if __name__ == "__main__":
    c = Controleur()
    # sans () objet mais execute pas tt de suite
