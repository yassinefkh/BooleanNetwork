# Boolean Network Simulator

---

## Description

This project is a Python-based Boolean Network Simulator that models the evolution of Boolean networks over time. Boolean networks are mathematical models used to describe the dynamics of complex systems, such as gene regulatory networks. In a Boolean network, each node represents a biological component, such as a gene or a protein, and is associated with a Boolean state (either True or False). The connections between nodes represent regulatory interactions, and the evolution of the network is governed by Boolean functions that determine the state of each node based on the states of its input nodes.

---

## Key Features

- **Node Representation:** Nodes in the Boolean network are represented as objects with the following attributes:

  - State: Boolean value representing the current state of the node (True or False).
  - Inputs: List of indices or pointers to the input nodes that influence the state of the current node.
  - Boolean Function Index: Index indicating the Boolean function used to compute the state of the node.

- **Boolean Functions:** Four basic Boolean functions are implemented:

  1. AND Gate
  2. OR Gate
  3. NOT Gate
  4. XOR Gate

- **Network Evolution:** The network evolves over time by applying the Boolean functions to each node based on the states of its input nodes.

- **Random Network Generation:** Option to generate a random Boolean network with specified connectivity and size.

- **Visualization:** Visualization of the Boolean network using NetworkX and Matplotlib, with nodes represented as circles and edges as arrows.

---

## Mathematical Notations

- **Boolean Functions:**

  - **AND Gate (A · B):** Returns True if both A and B are True, False otherwise.
  - **OR Gate (A + B):** Returns True if at least one of A and B is True, False otherwise.
  - **NOT Gate (¬A):** Returns the negation of A.
  - **XOR Gate (A ⊕ B):** Returns True if A and B have different values, False otherwise.

- **Boolean Network Evolution:**
  - At each time step, the state of each node is updated based on the states of its input nodes and the assigned Boolean function.
