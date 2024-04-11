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
        return inputs[0] != inputs[1]

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
