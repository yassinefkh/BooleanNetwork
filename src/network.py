from vertex import Vertex
import random  


class Network:
    
    def __init__(self, size, connectivity, is_homogeneous=True):
        """
        Initializes a network with specified size and connectivity.

        Args:
            size (int): Number of vertices in the network.
            connectivity (int): Number of inputs each vertex receives.
            is_homogeneous (bool, optional): If True, creates a homogeneous network where each vertex has the same number of inputs. 
                                              If False, creates a non-homogeneous network with varying inputs per vertex. Defaults to True.
        """
        self.size = size
        self.connectivity = connectivity
        self.network = [Vertex(connectivity, random.randint(0, 15)) for _ in range(size)]
        if is_homogeneous:
            self.create_homogeneous_network()
        else:
            self.create_non_homogeneous_network()
            
            
    def create_network(self):
        """
        Creates the network by initializing vertices with random connections.
        """
        # create vertices with a random boolean function among those available
        self.network = [Vertex(self.connectivity, random.randint(0, 15)) for i in range(self.size)]
        
        # add random connections
        for vertex in self.network:
            while len(vertex.inputs) < self.connectivity:
                k = random.randint(0, self.size - 1)
                # Avoiding redundant connections and self-connections
                if k not in vertex.inputs and k != self.network.index(vertex):
                    vertex.add_input(k)

    def create_homogeneous_network(self):
        """
        Creates a homogeneous network where each vertex has the same number of inputs.
        """
        k = self.connectivity
        for vertex in self.network:
            possible_inputs = list(range(self.size))
            possible_inputs.remove(self.network.index(vertex))
            vertex.inputs = random.sample(possible_inputs, k)

    def create_non_homogeneous_network(self):
        """
        Creates a non-homogeneous network with varying inputs per vertex.
        """
        for vertex in self.network:
            possible_inputs = list(range(self.size))
            possible_inputs.remove(self.network.index(vertex))
            k = random.randint(1, self.connectivity)
            vertex.inputs = random.sample(possible_inputs, k)

    def mutate_random_functions(self, mutation_rate=0.1):
        """
        Randomly mutates boolean functions of vertices in the network.

        Args:
            mutation_rate (float, optional): Mutation rate, i.e., the proportion of vertices to mutate. Defaults to 0.1.
        """
        num_mutations = int(self.size * mutation_rate)
        mutated_vertices = random.sample(self.network, num_mutations)
        for vertex in mutated_vertices:
            new_func_index = random.randint(0, 15)
            vertex.change_function(new_func_index)


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
        return ''.join(('1' if vertex.state else ' ') for vertex in self.network)
    # 1 represent active nodes, empty spaces inactive, non-ignited nodes
    
    def detect_attractors(self, states):
        """
        Detects attractors in the network states.

        Args:
            states (list): List of states to analyze.

        Returns:
            list: List of attractors found in the states.
        """
        attractors = []
        for i, state in enumerate(states):
            attractor_found = False
            for j in range(i + 1, len(states)):
                if state == states[j]:
                    attractors.append(states[i:j])
                    attractor_found = True
                    break
            if attractor_found:
                break
        return attractors
    
   
    
def simulate(size, connectivity, num_steps, is_homogeneous=True):
    """
    Simulates the network dynamics over a specified number of steps.

    Args:
        size (int): Number of vertices in the network.
        connectivity (int): Number of inputs each vertex receives.
        num_steps (int): Number of steps to simulate.
        is_homogeneous (bool, optional): If True, creates a homogeneous network where each vertex has the same number of inputs. 
                                          If False, creates a non-homogeneous network with varying inputs per vertex. Defaults to True.
    """
    network = Network(size, connectivity, is_homogeneous)
    network.display_connections()
    for i in range(num_steps):
        network.mutate_random_functions(mutation_rate=0.02)
        print(network)
        network.step()

if __name__ == "__main__":
    size = 20
    connectivity = 5
    num_steps = 100
    simulate(size, connectivity, num_steps)
