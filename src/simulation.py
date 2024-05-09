from network import Network  
import random
import pandas as pd
from collections import defaultdict
import csv
import itertools


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
        
        
        
def simulate_and_detect_attractors(size, connectivity, num_steps, num_trials, is_homogeneous=True, mutation_rate=0.02, display_evolution=True):
    """
    Simulates the network multiple times and detects attractors, with an option to display the evolution of the network states.

    Args:
        size (int): The number of vertices in the network.
        connectivity (int): The maximum number of incoming connections for each vertex.
        num_steps (int): The number of steps to simulate the network.
        num_trials (int): The number of trials to perform the simulation.
        is_homogeneous (bool): Whether the network is homogeneous.
        mutation_rate (float): Mutation rate for the random function.
        display_evolution (bool): Whether to display the evolution of the network states.

    Returns:
        list: A list of attractors detected in each trial.
    """

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


def run_simulations(params, display_evolution=True):
    results = []
    for size, connectivity, num_steps, num_trials, mutation_rate in params:
        for trial in range(num_trials):
            attractors = simulate_and_detect_attractors(size, connectivity, num_steps, 1, mutation_rate=mutation_rate, display_evolution=display_evolution)
            result = {
                'size': size,
                'connectivity': connectivity,
                'num_steps': num_steps,
                'trial': trial,
                'mutation_rate': mutation_rate,
                'attractors': attractors[0]
            }
            results.append(result)
    return results


def save_results_to_csv(results, filename):
    keys = results[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)


if __name__ == "__main__":
    sizes = [20, 50, 100]  
    connectivities = [2, 5, 10] 
    num_steps = [50, 100, 150] 
    num_trials = [5, 10, 20]  
    mutation_rates = [0.01, 0.03, 0.05] 

    params = list(itertools.product(sizes, connectivities, num_steps, num_trials, mutation_rates))
                   
    results = run_simulations(params)

    save_results_to_csv(results, 'results.csv')


""" if __name__ == "__main__":
    size = 20
    connectivity = 2
    num_steps = 100
    mutation_rate = 0.00
    num_trials = 3
    attractors = simulate_and_detect_attractors(size, connectivity, num_steps, num_trials, mutation_rate=mutation_rate)
    print("Attracteurs détectés :", attractors)
    attractor_counts = analyze_attractors(attractors)
    print("Attractor counts:", attractor_counts)
 """


""" if __name__ == "__main__":
    size = int(input("Enter the number of vertices in the network: "))
    connectivity = int(input("Enter the maximum number of incoming connections for each vertex: "))
    num_steps = int(input("Enter the number of steps to simulate the network: "))
    num_trials = int(input("Enter the number of trials to perform the simulation: "))
    is_homogeneous_input = input("Should the network be homogeneous? (yes/no): ").strip().lower() == 'yes'
    mutation_rate = float(input("Enter the mutation rate for the random function (e.g., 0.02): "))
    
    attractors = simulate_and_detect_attractors(size, connectivity, num_steps, num_trials, is_homogeneous=is_homogeneous_input, mutation_rate=mutation_rate)
    print("Detected attractors:", attractors) """