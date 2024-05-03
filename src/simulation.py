from network import Network  

def simulate(size, connectivity, num_steps, is_homogeneous=True):
    """
    Simulates the network for a given number of steps.

    Args:
        size (int): The number of vertices in the network.
        connectivity (int): The maximum number of incoming connections for each vertex.
        num_steps (int): The number of steps to simulate.
        is_homogeneous (bool): Whether the network should be homogeneous.
    """
    network = Network(size, connectivity, is_homogeneous)
    network.display_connections()
    for i in range(num_steps):
        network.mutate_random_functions(mutation_rate=0.05)  # apply random mutations at a specified rate
        print(network)
        network.step()
        
        
def simulate_and_detect_attractors(size, connectivity, num_steps, is_homogeneous=True, mutation_rate=0.02):
    """
    Simulates the network for a given number of steps and detects attractors.

    Args:
        size (int): The number of vertices in the network.
        connectivity (int): The maximum number of incoming connections for each vertex.
        num_steps (int): The number of steps to simulate.
        is_homogeneous (bool): Whether the network should be homogeneous.
        mutation_rate (float): The mutation rate for the random function.
    """
    network = Network(size, connectivity, is_homogeneous)
    network.display_connections()
    states = []
    for i in range(num_steps):
        network.mutate_random_functions(mutation_rate=mutation_rate)
        network.step()
        states.append(str(network))  
        print(network)  
    attractors = network.detect_attractors(states)
    return attractors

""" if __name__ == "__main__":
    size = 20
    connectivity = 5
    num_steps = 100
    simulate(size, connectivity, num_steps)
 """

if __name__ == "__main__":
    size = 20
    connectivity = 2
    num_steps = 100
    mutation_rate = 0.00
    attractors = simulate_and_detect_attractors(size, connectivity, num_steps, mutation_rate=mutation_rate)
    print("Attracteurs détectés :", attractors)
