from network import Network  
import random
import pandas as pd
from collections import defaultdict

def initialize_random_states(network):
    for vertex in network.network:
        vertex.state = random.choice([True, False])



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
        
        
        
def simulate_and_detect_attractors(size, connectivity, num_steps, num_trials, is_homogeneous=True, mutation_rate=0.02):
    """
    Simulates the network multiple times and detects attractors, with an option to display the evolution of the network states.

    Args:
        size (int): The number of vertices in the network.
        connectivity (int): The maximum number of incoming connections for each vertex.
        num_steps (int): The number of steps to simulate the network.
        num_trials (int): The number of trials to perform the simulation.
        is_homogeneous (bool): Whether the network is homogeneous.
        mutation_rate (float): Mutation rate for the random function.

    Returns:
        list: A list of attractors detected in each trial.
    """
  
    display_evolution = input("Do you want to display the evolution of the network states? (yes/no): ").strip().lower() == 'yes'
    
    attractors_results = []
    for trial in range(num_trials):
        network = Network(size, connectivity, is_homogeneous)
        initialize_random_states(network)  # random initial states
        network.display_connections()
        states = []
        for step in range(num_steps):
            network.mutate_random_functions(mutation_rate=mutation_rate)
            network.step()
            states.append(str(network))
            if display_evolution:
                print(f"{network}")
        attractors = network.detect_attractors(states)
        attractors_results.append(attractors)
        if display_evolution:
            print(f"\nAttractors for trial {trial + 1}: {attractors}\n")
    return attractors_results


def analyze_attractors(attractors_results):
    attractor_counts = defaultdict(int)
    for attractors in attractors_results:
        for attractor in attractors:
            if len(attractor) == 1:
                attractor_type = 'stable'
            else:
                attractor_type = 'periodic'
            attractor_counts[(attractor_type, tuple(attractor))] += 1
    return attractor_counts

if __name__ == "__main__":
    size = 20
    connectivity = 2
    num_steps = 100
    mutation_rate = 0.00
    num_trials = 3
    attractors = simulate_and_detect_attractors(size, connectivity, num_steps, num_trials, mutation_rate=mutation_rate)
    print("Attracteurs détectés :", attractors)
    attractor_counts = analyze_attractors(attractors)
    print("Attractor counts:", attractor_counts)



""" if __name__ == "__main__":
    size = int(input("Enter the number of vertices in the network: "))
    connectivity = int(input("Enter the maximum number of incoming connections for each vertex: "))
    num_steps = int(input("Enter the number of steps to simulate the network: "))
    num_trials = int(input("Enter the number of trials to perform the simulation: "))
    is_homogeneous_input = input("Should the network be homogeneous? (yes/no): ").strip().lower() == 'yes'
    mutation_rate = float(input("Enter the mutation rate for the random function (e.g., 0.02): "))
    
    attractors = simulate_and_detect_attractors(size, connectivity, num_steps, num_trials, is_homogeneous=is_homogeneous_input, mutation_rate=mutation_rate)
    print("Detected attractors:", attractors) """