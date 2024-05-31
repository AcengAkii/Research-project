#Code used to generate graphs and adjacency matrices

import numpy as np
import itertools
import networkx as nx #
import matplotlib.pyplot as plt
import math

def is_valid_graph(adj_matrix):
    n = len(adj_matrix)
    # Check if the matrix is symmetric
    if any(adj_matrix[i][j] != adj_matrix[j][i] for i in range(n) for j in range(n)):
        return False
    # Check if the diagonal elements are all zeros
    if any(adj_matrix[i][i] != 0 for i in range(n)):
        return False
    return True

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

    plt.savefig(f'graph1111_{matrix}')
    plt.show()
    plt.clf()
            
    print()
    
    return 

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

# Define the size of the graphs
n = 4  # Change this value to the desired size

# Generate and print all possible graphs of size n
num_graphs = generate_all_graphs(n)

print("Total number of graphs:", num_graphs[0])
all_matrices =  num_graphs[1]
print(all_matrices)


#to find the homomorphic graphs
import numpy as np
from collections import defaultdict

def row_counts(matrix):    #to group the matricess according to degree on each vertex
    matrix = np.array(matrix)
    n = len(matrix)  # Number of rows
    counts = []
    
    for i in range(n):
        ones_count = np.sum(matrix[i, :] == 1)
        zeros_count = np.sum(matrix[i, :] == 0)
        counts.append((zeros_count, ones_count))
    
    return tuple(counts)



def z1(matrix):     #count all the ones in the matrix, count all the zeros in the matrix
    matrix = np.array(matrix)
    count =[]
    oone = np.sum(matrix == 1)
    zzero = np.sum(matrix == 0)
    count.append((zzero,oone))
    
    return tuple(count)

def group(adj_matrices):     #to find homomorphic
    
    grouped_matrices = defaultdict(list) #creating an empty list
    
    for matrix in adj_matrices:
        counts = z1(matrix)                        
        grouped_matrices[counts].append(matrix)
        
    grouped_matrices = dict(grouped_matrices)
    nnn = len(grouped_matrices)

    return grouped_matrices,nnn


grouped, number_of_grps = group(all_matrices)

print(f'We can expect {number_of_grps} groups of graphs.')
print()

# Print each group of matrices
for counts, matrices_list in grouped.items():
    print(f"Group with counts {counts}:")
    for matrix in matrices_list:
        A = np.array(matrix)
        print(A)
        #dd = draw_graph(A)
        print()
    
