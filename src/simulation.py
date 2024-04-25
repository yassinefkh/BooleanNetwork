import random
from reseau import Reseau

def simuler(taille, connectivite, nb_etapes):
    reseau = Reseau(taille, connectivite)
    for i in range(nb_etapes):
        print(reseau)
        reseau.etape()  

        
        
if __name__ == "__main__":
    taille = 20 
    connectivite = 2
    nb_etapes = 10
    simuler(taille, connectivite, nb_etapes)