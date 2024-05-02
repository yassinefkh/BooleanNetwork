from sommet import Sommet
import random


class Reseau:
    def __init__(self, taille, connectivite):
        self.taille = taille
        self.connectivite = connectivite
        self.reseau = []
        self.creer_reseau()

    def creer_reseau(self):
        self.reseau = [Sommet(self.connectivite, i % 3) for i in range(self.taille)]  # 3 fct ici
        for i in range(self.taille):
            for j in range(self.connectivite):
                k = int(self.taille * random.random())
                self.reseau[i].ajouter_input(k)

    def etape(self):
        for s in self.reseau:
            s.appliquer_fonction(self.reseau)
            
    def afficher_liaisons(self):
        for i, sommet in enumerate(self.reseau):
            print(f"Sommet {i} : {sommet.inputs}")

    """ 
    def __str__(self):
        return ''.join(f'{sommet.func_index:2} ' + ('●' if sommet.etat else '○') for sommet in self.reseau)
    """
    def __str__(self):
        return ''.join(('1' if sommet.etat else ' ') for sommet in self.reseau)


def simuler(taille, connectivite, nb_etapes):
    reseau = Reseau(taille, connectivite)
    reseau.afficher_liaisons()
    for i in range(nb_etapes):
        print(reseau)
        for j in range(taille):
            func_index = int(input(f"Entrez l'index de la fonction booléenne à appliquer au sommet {j} (0: NAND, 1: AND, 2: XOR, 3: INDENTITY) : "))
            reseau.reseau[j].changer_fonction(func_index)
        reseau.etape()

if __name__ == "__main__":
    taille = 6
    connectivite = 3
    nb_etapes = 10
    simuler(taille, connectivite, nb_etapes)