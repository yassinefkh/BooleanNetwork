from network import Network  

def simulate(size, connectivity, num_steps):
    """
    Simulates the network for a given number of steps.

    Args:
        size (int): The number of vertices in the network.
        connectivity (int): The maximum number of incoming connections for each vertex.
        num_steps (int): The number of steps to simulate.
    """
    network = Network(size, connectivity)
    network.display_connections()
    for i in range(num_steps):
        print(network)
        network.step()

if __name__ == "__main__":
    size = 20
    connectivity = 5
    num_steps = 100
    simulate(size, connectivity, num_steps)
