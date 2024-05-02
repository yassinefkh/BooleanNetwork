import random

class Sommet:
    def __init__(self, nb_inputs, func_index):
        self.etat = False
        self.nb_inputs = nb_inputs
        self.inputs = []
        self.func_index = func_index
        self.historique_fonctions = []

    def ajouter_input(self, index):
        self.inputs.append(index)

    def changer_etat(self):
        self.etat = not self.etat

    def appliquer_fonction(self, reseau):
        args = [reseau[i].etat for i in self.inputs]
        self.etat = self.calculer_etat(args)
        self.historique_fonctions.append(self.func_index)

    def calculer_etat(self, inputs):
        if self.func_index == 0:  # Fonction NAND
            return not all(inputs)
        elif self.func_index == 1:  # Fonction AND
            return all(inputs)
        elif self.func_index == 2:  # Fonction XOR
            return sum(inputs) % 2 == 1
        elif self.func_index == 3:  # Fonction Identité
            return inputs[0]  
        else:
            raise ValueError("Index de fonction non valide")

    def __str__(self):
        return str(int(self.etat))
    
    def changer_fonction(self, func_index):
        self.func_index = func_index
