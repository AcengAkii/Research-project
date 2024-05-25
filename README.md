# Research-project
Ramsey numbers : For the classical algorithm
import numpy as np
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def is_valid_graph(adj_matrix):
    n = len(adj_matrix)
    # Check if the matrix is symmetric
    if any(adj_matrix[i][j] != adj_matrix[j][i] for i in range(n) for j in range(n)):
        return False
    # Check if the diagonal elements are all zeros
    if any(adj_matrix[i][i] != 0 for i in range(n)):
        return False
    return True

def generate_all_graphs(n):
    count = 0
    # Generate all possible binary matrices of size n x n
    binary_matrices = itertools.product([0, 1], repeat=n*n)
    
    for matrix in binary_matrices:
        # Reshape the binary matrix into a square matrix
        adj_matrix = [matrix[i:i+n] for i in range(0, len(matrix), n)]
        
        # Check if the matrix represents a valid graph
        if is_valid_graph(adj_matrix):
            count += 1
            print(adj_matrix)
            # Create an empty graph
            G = nx.Graph()
            # Add nodes
            G.add_nodes_from(range(n))
            # Add edges
            for i in range(n):
                for j in range(i+1, n):
                    if adj_matrix[i][j] == 1:
                        G.add_edge(i, j)
            
            # Print the graph
            print("Graph:")
            print(G.edges())
            #print() #print the list of non-edges
            
            # Visualize the graph
            nx.draw(G, with_labels=True)
            plt.title("Graph Visualization")
            
            plt.savefig(f'graph1111_{matrix}')
            plt.show()
            plt.clf()
            
            
            print()
       
    return count

# Define the size of the graphs
n = 4  # Change this value to the desired size

# Generate and print all possible graphs of size n
num_graphs = generate_all_graphs(n)
print("Total number of graphs:", num_graphs)
