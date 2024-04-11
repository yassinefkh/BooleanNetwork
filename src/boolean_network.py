from boolean_network_vertex import BooleanNetworkVertex
import random

class BooleanNetwork:
    def __init__(self, connectivity, size):
        self.vertices = []
        self.connectivity = connectivity
        self.size = size

    def AND_gate(self, inputs):
        return all(inputs)

    def OR_gate(self, inputs):
        return any(inputs)

    def NOT_gate(self, inputs):
        return not inputs[0]

    def XOR_gate(self, inputs):
        if len(inputs) >= 2:
            return inputs[0] != inputs[1]
        else:
            return False  


    def create(self):
        for _ in range(self.size):
            vertex = BooleanNetworkVertex(random.choice([True, False]), [], random.randint(0, self.connectivity - 1))
            self.vertices.append(vertex)

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def remove_vertex(self, index):
        del self.vertices[index]

    def get_vertex(self, index):
        return self.vertices[index]

    def connect_vertices(self, source, target):
        source_vertex = self.get_vertex(source)
        target_vertex = self.get_vertex(target)
        target_vertex.inputs.append(source)
        source_vertex.inputs.append(target)

    def disconnect_vertices(self, source, target):
        source_vertex = self.get_vertex(source)
        target_vertex = self.get_vertex(target)
        target_vertex.inputs.remove(source)
        source_vertex.inputs.remove(target)

    def init_states(self, states):
        for i, state in enumerate(states):
            self.vertices[i].state = state

    def generate_random_network(self):
        self.create()
        for _ in range(self.size):
            source = random.randint(0, self.size - 1)
            target = random.randint(0, self.size - 1)
            self.connect_vertices(source, target)
            
    def assign_boolean_functions(self):
        boolean_functions = [self.AND_gate, self.OR_gate, self.NOT_gate, self.XOR_gate]
        for vertex in self.vertices:
            vertex.bool_func_index = random.randint(0, len(boolean_functions) - 1)
            vertex.boolean_function = boolean_functions[vertex.bool_func_index]
            print(f"Node {self.vertices.index(vertex)} assigned boolean function: {vertex.boolean_function.__name__}")


    def apply_boolean_functions(self):
        for vertex in self.vertices:
            input_states = [self.vertices[i].state for i in vertex.inputs]
            vertex.state = vertex.boolean_function(input_states)

    def evolve_network(self):
        self.assign_boolean_functions()
        for _ in range(self.size):  
            self.apply_boolean_functions()
