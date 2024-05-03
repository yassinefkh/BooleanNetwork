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

if __name__ == "__main__":
    size = 20
    connectivity = 5
    num_steps = 100
    simulate(size, connectivity, num_steps)
