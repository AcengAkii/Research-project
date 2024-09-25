# This file groups adjacency matrices that are 
# homomorphic to one another. 

import numpy as np
import function_drawing as dr
from collections import defaultdict
import networkx as nx
import itertools
import function_adjacency as aj

#A counting function - to determine the edge sequences
def ones_per_row(matrix): #Another way to find the 'degree' of a vertex
    return [row.count(1) for row in matrix]

#Function takes in a list of matrices---
def group_matrices_by_ones(matrices): #regardless of row order group the matrices, according to ones per row.
    groups = defaultdict(list) 
    llist = []
    keeys = []
    
    for matrix in matrices:
        ones_count = ones_per_row(matrix)
        ones_count_sorted = tuple(sorted(ones_count))
        groups[ones_count_sorted].append(matrix)

    for key, group in groups.items():
        A = np.array(group)
        ####################################################
        #uncomment this for a pretty view
        
        # print(f"Group {key}:")
        # print(f"representative matrix")
        # print()
        # print(A[0])

        # #To draw the graph
        # B = dr.draw_graph(A[0])
        # print("=" * 40)
        
        #####################################################
        
        llist.append(A[0].tolist())
        keeys.append(key)
        
    nnn = len(groups)
    
    print(f'We can expect {nnn} groups of graphs.')
    #print()
    
        
    return llist, keeys









def count_non_isomorphic_graphs(graphs):
    """
    Count the number of non-isomorphic graphs given a list of adjacency matrices represented as lists of lists.
    
    Args:
        graphs (list of lists): A list of adjacency matrices representing graphs.
        
    Returns:
        int: Number of non-isomorphic graphs.
        list: List of unique non-isomorphic graphs.
    """
    # Create a list to store unique (non-isomorphic) graphs
    unique_graphs = []
    
    for graph in graphs:
        # Assume the graph is unique until proven otherwise
        is_unique = True
        for unique_graph in unique_graphs:
            # Check for isomorphism by permuting the adjacency matrix
            if check_isomorphism(graph, unique_graph):
                is_unique = False
                break
        
        # If it is unique, add it to the list
        if is_unique:
            unique_graphs.append(graph)

    return len(unique_graphs), unique_graphs


def check_isomorphism(adj_matrix1, adj_matrix2):
    """
    Check if two graphs are isomorphic by comparing adjacency matrices represented as lists of lists.
    
    Args:
        adj_matrix1 (list of lists): Adjacency matrix of the first graph.
        adj_matrix2 (list of lists): Adjacency matrix of the second graph.
        
    Returns:
        bool: True if the graphs are isomorphic, False otherwise.
    """
    n = len(adj_matrix1)  # Number of nodes
    
    # Generate all possible permutations of node indices
    for perm in itertools.permutations(range(n)):
        # Create a permuted adjacency matrix for adj_matrix1
        permuted_matrix = [[adj_matrix1[i][j] for j in perm] for i in perm]
        
        # Check if the permuted matrix is equal to the second adjacency matrix
        if permuted_matrix == adj_matrix2:
            return True

    return False





def divide_list(lst, num_lists):
    """
    Divides a list into a specified number of smaller lists.
    
    Args:
        lst (list): The input list to be divided.
        num_lists (int): The number of smaller lists to create.
        
    Returns:
        list: A list of smaller lists.
    """
    chunk_size = len(lst) // num_lists
    remainder = len(lst) % num_lists
    
    divided_lists = []
    start = 0
    
    for i in range(num_lists):
        end = start + chunk_size
        if i < remainder:
            end += 1
        divided_lists.append(lst[start:end])
        start = end
    
    return divided_lists

def merge_lists(lists):
    """
    Merges multiple lists into a single list.
    
    Args:
        lists (list): A list of lists to be merged.
        
    Returns:
        list: A single merged list.
    """
    merged_list = []
    for lst in lists:
        merged_list.extend(lst)
    return merged_list

