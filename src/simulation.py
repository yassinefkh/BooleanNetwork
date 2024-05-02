from reseau import Reseau

def simuler(taille, connectivite, nb_etapes):
    reseau = Reseau(taille, connectivite)
    reseau.afficher_liaisons()
    for i in range(nb_etapes):
        print(reseau)
        reseau.etape()

if __name__ == "__main__":
    taille = 10
    connectivite = 4
    nb_etapes = 50
    simuler(taille, connectivite, nb_etapes)
