import random

class Vertex:
    def __init__(self, num_inputs, func_index):
        """
        Initializes a vertex in the network.

        Args:
            num_inputs (int): The number of inputs for the vertex.
            func_index (int): The index representing the boolean function to be applied.
        """
        self.state = False
        self.num_inputs = num_inputs
        self.inputs = []
        self.func_index = func_index
        self.function_history = []

    def add_input(self, index):
        """
        Adds an input connection to the vertex.

        Args:
            index (int): The index of the connected vertex.
        """
        self.inputs.append(index)

    def change_state(self):
        """Changes the state of the vertex."""
        self.state = not self.state

    def apply_function(self, network):
        """
        Applies the boolean function to the vertex based on its inputs.

        Args:
            network (list): The list of vertices representing the network.
        """
        args = [network[i].state for i in self.inputs]
        self.state = self.calculate_state(args)
        self.function_history.append(self.func_index)

    def calculate_state(self, inputs):
        """
        Calculates the state of the vertex based on its inputs and the selected boolean function.

        Args:
            inputs (list): The list of input states.

        Returns:
            bool: The calculated state of the vertex.
        """
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
            raise ValueError("Invalid function index")

    def __str__(self):
        """
        Returns the string representation of the state of the vertex.

        Returns:
            str: The string representation of the state (either '1' or '0').
        """
        return str(int(self.state))
    
    def change_function(self, func_index):
        """
        Changes the boolean function of the vertex.

        Args:
            func_index (int): The index representing the new boolean function.
        """
        self.func_index = func_index
