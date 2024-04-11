import networkx as nx
import matplotlib.pyplot as plt

def visualize_boolean_network(network):
    G = nx.DiGraph()
    for i, vertex in enumerate(network.vertices):
        G.add_node(f"Vertex {i}", state=vertex.state)
    for i, vertex in enumerate(network.vertices):
        for input_vertex_index in vertex.inputs:
            G.add_edge(f"Vertex {input_vertex_index}", f"Vertex {i}")

    pos = nx.spring_layout(G)
    node_colors = ["red" if G.nodes[node]["state"] else "blue" for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color=node_colors, font_size=10, font_weight="bold")
    plt.show()
