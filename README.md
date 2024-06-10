# Graphs and Adjacency Matrices
The code below will print out all the graphs and adjacency matrices.

#Code used to generate graphs and adjacency matrices

import numpy as np
import itertools
import networkx as nx #
import matplotlib.pyplot as plt
import math

#function 1
def is_valid_graph(adj_matrix):
    n = len(adj_matrix)
    # Check if the matrix is symmetric
    if any(adj_matrix[i][j] != adj_matrix[j][i] for i in range(n) for j in range(n)):
        return False
    # Check if the diagonal elements are all zeros
    if any(adj_matrix[i][i] != 0 for i in range(n)):
        return False
    return True

#function 2
def draw_graph(adj_matrix):
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

    if n == 1:
        pos = {0:(0.5,0.5)}
    elif n ==2:
        pos = {0:(0,1), 1:(1,1)}
        colour = 'green'
    elif n == 3:
        pos = {0:(0,1) , 1:(1,1), 2:(0,0)}
        colour = 'blue'
    elif n ==4:
        pos = {0:(0,1) , 1:(1,1), 2:(0,0) , 3:(1,0)}
        colour = 'red'
    elif n == 5:
        pos = {0:(0,1) , 1:(1,1), 2:(0,0) , 3:(1,0), 4:(0.5, 1+ math.sqrt(4/5))}
        colour = 'black'

    # Visualize the graph
    nx.draw(G, pos , edge_color = colour, width = 3,with_labels=True)
    plt.title("Graph Visualization")

    plt.savefig(f'graph1111_{adj_matrix}')
    plt.show()
    plt.clf()
            
    print()
    
    return 
    
#function 3
def generate_all_graphs(n):
    count = 0
    # Generate all possible binary matrices of size n x n
    binary_matrices = itertools.product([0, 1], repeat=n*n)
    all_matrices = [] # list to store the valid matrices.
    
    for matrix in binary_matrices:
        
        
        # Reshape the binary matrix into a square matrix
        adj_matrix = [matrix[i:i+n] for i in range(0, len(matrix), n)]
        
        # Check if the matrix represents a valid graph
        if is_valid_graph(adj_matrix):
            count += 1
            print(adj_matrix)
            #store the adjacency matrix in a list.
            all_matrices.append(adj_matrix)
            
            graphs = draw_graph(adj_matrix)
            print()
       
    return count,all_matrices

    #Test it out
# Define the size of the graphs
n = 4  # Change this value to the desired size

# Generate and print all possible graphs of size n
num_graphs = generate_all_graphs(n)

print("Total number of graphs:", num_graphs[0])
all_matrices =  num_graphs[1]
print(all_matrices)

# Homomorphic Graphs
The code below should group together all homomorphic graphs and print out 1 graph as a representative of each group.

#to find the homomorphic graphs
import numpy as np
from collections import defaultdict

#function 2 - ***
def ones_per_row(matrix): #Another way to find the 'degree' of a vertex
    return [row.count(1) for row in matrix]
    
#function 3 - ***
def group_matrices_by_ones(matrices): #regardless of row order group the matrices, according to ones per row.
    groups = defaultdict(list)
    
    for matrix in matrices:
        ones_count = ones_per_row(matrix)
        ones_count_sorted = tuple(sorted(ones_count))
        groups[ones_count_sorted].append(matrix)

    nnn = len(groups)
    return groups, nnn

#Test it out
grouped, number_of_grps = group_matrices_by_ones(all_matrices)

print(f'We can expect {number_of_grps} groups of graphs.')
print()

#print groups of adjacency matrices

# nnn = len(all_matrices)
# for k in range(nnn): 
#     matrix = all_matrices[k]  
#     a = draw_graph(matrix)
#     print(a)

for key, group in grouped.items(): #To print out the homomorphic adjacency graphs
    print(f"Group {key}:")
    group = np.array(group)
    print(group)
    print("=" * 40) 

 # Draw 1 graph from each set of Homomorphic graphs
