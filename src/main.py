from boolean_network import BooleanNetwork
from boolean_network_visualization import visualize_boolean_network

def main():
   
    network = BooleanNetwork(connectivity=2, size=5)

    network.generate_random_network()

    visualize_boolean_network(network)

if __name__ == "__main__":
    main()
