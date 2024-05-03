from vertex import Vertex 
import random  


class Network:
    def __init__(self, size, connectivity):
        """
        Initializes the Network class.

        Args:
            size (int): The number of vertices in the network.
            connectivity (int): The maximum number of incoming connections for each vertex.
        """
        self.size = size
        self.connectivity = connectivity
        self.network = []  # List to store the vertices of the network
        self.create_network()  # Calling the method to create the network

    def create_network(self):
        """
        Creates the network by initializing vertices with random connections.
        """
        # Creating vertices with a random boolean function among those available
        self.network = [Vertex(self.connectivity, random.randint(0, 15)) for i in range(self.size)]
        
        # Adding random connections
        for vertex in self.network:
            while len(vertex.inputs) < self.connectivity:
                k = random.randint(0, self.size - 1)
                # Avoiding redundant connections and self-connections
                if k not in vertex.inputs and k != self.network.index(vertex):
                    vertex.add_input(k)

    def step(self):
        """
        Applies the boolean function to each vertex in the network.
        """
        for vertex in self.network:
            vertex.apply_function(self.network)
            
    def display_connections(self):
        """
        Displays the connections of each vertex in the network.
        """
        for i, vertex in enumerate(self.network):
            print(f"Vertex {i}: {vertex.inputs}")

    def __str__(self):
        """
        Returns a string representation of the network's state.
        """
        return ''.join(('■' if vertex.state else '□') for vertex in self.network)


def simulate(size, connectivity, num_steps):
    network = Network(size, connectivity)
    network.display_connections()
    for i in range(num_steps):
        print(network)
        for j in range(size):
            func_index = int(input(f"Enter the index of the boolean function to apply to vertex {j} (0: NAND, 1: AND, 2: XOR, 3: IDENTITY): "))
            network.network[j].change_function(func_index)
        network.step()

if __name__ == "__main__":
    size = 6
    connectivity = 4
    num_steps = 10
    simulate(size, connectivity, num_steps)
