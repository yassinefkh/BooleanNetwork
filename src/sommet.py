class Sommet:
    def __init__(self, nb_inputs, func_index):
        self.etat = False
        self.nb_inputs = nb_inputs
        self.inputs = []
        self.func_index = func_index

    def ajouter_input(self, index):
        self.inputs.append(index)

    def changer_etat(self):
        self.etat = not self.etat

    def appliquer_fonction(self, reseau):
        args = [reseau[i].etat for i in self.inputs]
        self.etat = self.fonctions_bool[self.func_index](args)

    def __str__(self):
        return str(int(self.etat))

    fonctions_bool = {
        0: lambda x: False,
        1: lambda x: x[0],
        2: lambda x: x[1],
        3: lambda x: x[0] and x[1],
        4: lambda x: not x[0] and x[1],
        5: lambda x: x[0] and not x[1],
        6: lambda x: x[0] or x[1],
        7: lambda x: not x[0] or x[1],
        8: lambda x: x[0] != x[1],
        9: lambda x: x[0] == x[1],
    }
