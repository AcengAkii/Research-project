#Code used to generate graphs and adjacency matrices

import numpy as np
import itertools
import networkx as nx #
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
            
            
            # Visualize the graph
            nx.draw(G, with_labels=True)
            plt.title("Graph Visualization")
            
            plt.savefig(f'graph1111_{matrix}')
            plt.show()
            plt.clf()
            

            
            print()
       
    return count,all_matrices

# Define the size of the graphs
n = 3  # Change this value to the desired size

# Generate and print all possible graphs of size n
num_graphs = generate_all_graphs(n)

print("Total number of graphs:", num_graphs[0])
all_matrices =  num_graphs[1]
print(all_matrices)


#to find the homomorphic graphs
import numpy as np
from collections import defaultdict



def homomorphic(adj_matrices):
    
    def row_counts(matrix): #count the 1s and 0s and store them
        counts = [(np.sum(row == 1), np.sum(row == 0)) for row in matrix]
        return tuple(counts)
    
    grouped_matrices = defaultdict(list) #creating an empty list
    
    for matrix in adj_matrices:
        counts = row_counts(matrix)
        grouped_matrices[counts].append(matrix)
    

    grouped_matrices = dict(grouped_matrices)
    
    #nnn = len(grouped_matrices)
    
    return grouped_matrices

a = homomorphic(all_matrices)
print(a)

#To find the k-cliques and l-indep sets

def rams(k,l):
    #add up the number of 1's and zeros above the main diagonal each row
    ones_count = [0] * n
    zeros_count = [0] * n

    #by adding the number of ones and zeros we could maybe find the degree of each vertex and then the cliques..
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                ones_count[i] +=1
            elif matrix[i][j] == 0 and i != j: #leave out the diagonal
                zeros[i] +=1
    
    # compare the elements of ones to find k
    
    
    # compare the elements of zeros to find l
    
    
    return N
