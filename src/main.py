from boolean_network import BooleanNetwork
from boolean_network_vertex import BooleanNetworkVertex
from boolean_network_visualization import visualize_boolean_network

def main():
    # Créer un réseau booléen avec deux nœuds
    network = BooleanNetwork(connectivity=2, size=2)
    
    
    
    # Créer les deux node avec les fonctions booléennes spécifiques
    # Par exemple, utiliser la fonction OR pour le premier nœud et la fonction AND pour le deuxième nœud
    vertex0 = BooleanNetworkVertex(state=True, inputs=[], bool_func_index=None)  # Premier nœud (vertex0)
    vertex1 = BooleanNetworkVertex(state=False, inputs=[0], bool_func_index=None) # Deuxième nœud (vertex1)
    
    # Ajouter les nœuds au réseau
    network.add_vertex(vertex0)
    network.add_vertex(vertex1)
    
    # Connecter les nœuds
    network.connect_vertices(source=0, target=1)
    
    # Définir les fonctions booléennes pour chaque node
    vertex0.boolean_function = network.OR_gate  # Définir la fonction booléenne OR pour le premier nœud
    vertex1.boolean_function = network.AND_gate # Définir la fonction booléenne AND pour le deuxième nœud
    
    print("États initiaux des nœuds :")
    for i, vertex in enumerate(network.vertices):
        print(f"Nœud {i}: État = {vertex.state}")
    
    print("\nFonctions booléennes attribuées aux nœuds :")
    for i, vertex in enumerate(network.vertices):
        print(f"Nœud {i}: Fonction booléenne = {vertex.boolean_function.__name__}")
    
    # Évoluer le réseau
    network.evolve_network()
    
    # Visualiser le réseau
    visualize_boolean_network(network)



if __name__ == "__main__":
    main()
