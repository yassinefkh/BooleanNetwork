import random
from reseau import Reseau

""" def simuler(taille, connectivite, nb_etapes):
    reseau = Reseau(taille, connectivite)
    for i in range(nb_etapes):
        print(reseau)
        reseau.etape()   """
        
""" def simuler(taille, connectivite, nb_etapes):
    reseau = Reseau(taille, connectivite)
    for i in range(nb_etapes):
        print(reseau)
        for j in range(taille):
            func_index = int(input(f"Entrez la fonction booléenne à appliquer au sommet {j} : "))
            reseau.reseau[j].changer_fonction(func_index)
        reseau.etape() """

def simuler(taille, connectivite, nb_etapes):
    reseau = Reseau(taille, connectivite)
    reseau.afficher_liaisons()
    for i in range(nb_etapes):
        print(reseau)
        for j in range(taille):
            func_index = int(input(f"Entrez la fonction booléenne à appliquer au sommet {j} : "))
            reseau.reseau[j].changer_fonction(func_index)
        reseau.etape()



        
if __name__ == "__main__":
    taille = 4
    connectivite = 1
    nb_etapes = 10
    simuler(taille, connectivite, nb_etapes)