from sommet import Sommet
import random

class Reseau:
    def __init__(self, taille, connectivite):
        self.taille = taille
        self.connectivite = connectivite
        self.reseau = []
        self.creer_reseau()

    def creer_reseau(self):
        self.reseau = [Sommet(self.connectivite, i % 9) for i in range(self.taille)] # on chsoit une fct bool aleatoire parmi les 9
        for i in range(self.taille):
            for j in range(self.connectivite):
                k = int(self.taille * random.random())
                self.reseau[i].ajouter_input(k)

    def etape(self):
        for s in self.reseau:
            s.appliquer_fonction(self.reseau)

    def __str__(self):
            return ''.join('●' if sommet.etat else '○' for sommet in self.reseau) 
        
    
