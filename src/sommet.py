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
        if self.func_index == 0:  # NULL function (always False)
            return False
        elif self.func_index == 1:  # AND
            return all(inputs)
        elif self.func_index == 2:  # OR
            return any(inputs)
        elif self.func_index == 3:  # XOR
            return sum(inputs) % 2 == 1
        elif self.func_index == 4:  # NAND
            return not all(inputs)
        elif self.func_index == 5:  # NOR
            return not any(inputs)
        elif self.func_index == 6:  # XNOR
            return sum(inputs) % 2 == 0
        elif self.func_index == 7:  # Identity of first input
            return inputs[0]
        elif self.func_index == 8:  # Inverse of first input
            return not inputs[0]
        elif self.func_index == 9:  # Identity of second input (or false if not available)
            return inputs[1] if len(inputs) > 1 else False
        elif self.func_index == 10:  # Inverse of second input (or false if not available)
            return not inputs[1] if len(inputs) > 1 else False
        elif self.func_index == 11:  # A AND NOT B
            return inputs[0] and not inputs[1] if len(inputs) > 1 else False
        elif self.func_index == 12:  # NOT A AND B
            return not inputs[0] and inputs[1] if len(inputs) > 1 else False
        elif self.func_index == 13:  # NOT A
            return not inputs[0]
        elif self.func_index == 14:  # NOT B
            return not inputs[1] if len(inputs) > 1 else False
        elif self.func_index == 15:  # TRUE (always True)
            return True
        else:
            raise ValueError("Index de fonction non valide")


    def __str__(self):
        return str(int(self.etat))
    
    def changer_fonction(self, func_index):
        self.func_index = func_index
