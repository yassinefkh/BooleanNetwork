from boolean_network_vertex import BooleanNetworkVertex 
import random

class BooleanNetwork:
    def __init__(self, connectivity, size):
        """
        Initializes a BooleanNetwork object.

        Parameters:
        - connectivity (int): The connectivity of the network.
        - size (int): The number of vertices in the network.
        """
        self.vertices = []  # list to store vertices
        self.connectivity = connectivity  # the average number of incoming edges per vertex
        self.size = size  # the number of vertices in the network

    def AND_gate(self, inputs):
        """
        Performs the AND operation on a list of inputs.

        Parameters:
        - inputs (list): List of Boolean inputs.

        Returns:
        - bool: True if all inputs are True, False otherwise.
        """
        return all(inputs)

    def OR_gate(self, inputs):
        """
        Performs the OR operation on a list of inputs.

        Parameters:
        - inputs (list): List of Boolean inputs.

        Returns:
        - bool: True if any input is True, False otherwise.
        """
        return any(inputs)

    def NOT_gate(self, inputs):
        """
        Performs the NOT operation on a single input.

        Parameters:
        - inputs (list): List containing a single Boolean input.

        Returns:
        - bool: True if the input is False, False if the input is True.
        """
        return not inputs[0]

    def XOR_gate(self, inputs):
        """
        Performs the XOR operation on two inputs.

        Parameters:
        - inputs (list): List containing two Boolean inputs.

        Returns:
        - bool: True if the inputs are different, False if the inputs are the same.
        """
        if len(inputs) >= 2:
            return inputs[0] != inputs[1]
        else:
            return False  

    def create(self):
        """
        Creates vertices with random initial states and connections.
        """
        for _ in range(self.size):
            vertex = BooleanNetworkVertex(random.choice([True, False]), [], random.randint(0, self.connectivity - 1))
            self.vertices.append(vertex)

    def add_vertex(self, vertex):
        """
        Adds a vertex to the network.

        Parameters:
        - vertex (BooleanNetworkVertex): The vertex to be added.
        """
        self.vertices.append(vertex)

    def remove_vertex(self, index):
        """
        Removes a vertex from the network.

        Parameters:
        - index (int): The index of the vertex to be removed.
        """
        del self.vertices[index]

    def get_vertex(self, index):
        """
        Retrieves a vertex from the network.

        Parameters:
        - index (int): The index of the vertex to be retrieved.

        Returns:
        - BooleanNetworkVertex: The vertex at the specified index.
        """
        return self.vertices[index]

    def connect_vertices(self, source, target):
        """
        Connects two vertices in the network.

        Parameters:
        - source (int): Index of the source vertex.
        - target (int): Index of the target vertex.
        """
        source_vertex = self.get_vertex(source)
        target_vertex = self.get_vertex(target)
        target_vertex.inputs.append(source)
        source_vertex.inputs.append(target)

    def disconnect_vertices(self, source, target):
        """
        Disconnects two vertices in the network.

        Parameters:
        - source (int): Index of the source vertex.
        - target (int): Index of the target vertex.
        """
        source_vertex = self.get_vertex(source)
        target_vertex = self.get_vertex(target)
        target_vertex.inputs.remove(source)
        source_vertex.inputs.remove(target)

    def init_states(self, states):
        """
        Initializes the states of vertices in the network.

        Parameters:
        - states (list): List of Boolean states for each vertex.
        """
        for i, state in enumerate(states):
            self.vertices[i].state = state

    def generate_random_network(self):
        """
        Generates a random network with random initial states and connections.
        """
        self.create()
        for _ in range(self.size):
            source = random.randint(0, self.size - 1)
            target = random.randint(0, self.size - 1)
            self.connect_vertices(source, target)
            
    def assign_boolean_functions(self):
        """
        Assigns random Boolean functions to each vertex in the network.
        """
        boolean_functions = [self.AND_gate, self.OR_gate, self.NOT_gate, self.XOR_gate]
        for vertex in self.vertices:
            vertex.bool_func_index = random.randint(0, len(boolean_functions) - 1)
            vertex.boolean_function = boolean_functions[vertex.bool_func_index]
            print(f"Node {self.vertices.index(vertex)} assigned boolean function: {vertex.boolean_function.__name__}")

    def apply_boolean_functions(self):
        """
        Applies Boolean functions to update the states of vertices in the network.
        """
        for vertex in self.vertices:
            input_states = [self.vertices[i].state for i in vertex.inputs]
            vertex.state = vertex.boolean_function(input_states)

    def evolve_network(self):
        """
        Evolves the network by assigning Boolean functions and applying them to update vertex states.
        """
        self.assign_boolean_functions()
        for _ in range(self.size):  
            self.apply_boolean_functions()
