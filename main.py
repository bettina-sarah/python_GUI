import random
from tkinter import *
from helper import Helper as hp

class Vue():
    def __init__(self, parent, modele):
        self.root = Tk()  # comme dans linux, . = root
        self.parent = parent #controleur
        self.modele = modele
        mavar = Label(self.root, text="bienvenue au cours de C31-intensif")
        mavar.pack()
        mavar2 = Button(self.root, text="Cours graphique", command=self.creer_pion_vue)
        mavar2.pack()

        mavar3 = Button(self.root, text="Deplacer", command=self.animer)
        mavar3.pack()
        # pack_forget (loading...)
        #canvas class: needs params: root, w, h, bg(background)
        self.canvas = Canvas(self.root, width=self.modele.largeur, height=self.modele.hauteur, bg="medium slate blue")
        self.canvas.bind("<Button>", self.get_position) # bouton SOURIS !
        self.canvas.pack()

    def animer(self):
        self.parent.animer()


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
            #tags = tuple () - pas liste, on peut pas modifier
            # (haha,) = tuple have to put , so python considers it a tuple - i.posX, i.posY
            self.canvas.create_rectangle(i.posX, i.posY,
                                         i.posX+i.taille, i.posY+i.taille, fill="DeepPink2",
                                         tags=("pion",))


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

    def deplacer_pions(self):
        for i in self.pions:
            i.deplacer()


class Pion():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.taille = 30
        self.vitesse = 5 # pas trop d'attribut hardcodé idealement
        self.posX = x
        self.posY = y
        self.cibleX = None
        self.cibleY = None
        self.angle = None

    def trouver_cible(self):
        self.cibleX = random.randrange(self.parent.largeur)
        self.cibleY = random.randrange(self.parent.hauteur)
        self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)

    def deplacer(self):
        if self.cibleX: # si pas de cible ... trouve une la
            self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)

            distance = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)

            if distance <= self.vitesse:
                self.trouver_cible()
        else:
            self.trouver_cible() # et prochaine iteration, calcule distance






class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.vue.root.mainloop()

    def creer_pion_controleur(self):
        self.modele.creer_pion_modele()
        self.vue.afficher_pions()
        print("nbr pions:", len(self.modele.pions))

    def deplacer_pions(self):
        self.modele.deplacer_pions()
        self.vue.afficher_pions()

    def animer(self):
        self.modele.deplacer_pions()
        self.vue.afficher_pions()
        self.vue.root.after(50, self.animer) # recurser overflow si on met ()



    # .after - comb de ms avant d'appeler la fonction, 2eme param: fonction
    # une asorte de async, on fait dautre chose en background
    # comment l'arreter, attribut avec loop en cours


if __name__ == "__main__":
    c = Controleur()
    # sans () objet mais execute pas tt de suite
