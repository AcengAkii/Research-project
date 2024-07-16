# This file groups adjacency matrices that are 
# homomorphic to one another. 

import numpy as np
from collections import defaultdict

#A counting function - edge sequences
def ones_per_row(matrix): #Another way to find the 'degree' of a vertex
    return [row.count(1) for row in matrix]

#Function takes in a list of matrices---
def group_matrices_by_ones(matrices): #regardless of row order group the matrices, according to ones per row.
    groups = defaultdict(list) 
    
    for matrix in matrices:
        ones_count = ones_per_row(matrix)
        ones_count_sorted = tuple(sorted(ones_count))
        groups[ones_count_sorted].append(matrix)

    for key, group in groups.items():
        print(f"Group {key}:")
        print(f"representative matrix")
        print()
        A = np.array(group)
        print(A[0])

        #To draw the graph
        #B = draw_graph(A[0])
        #print(B)
        print("=" * 40)
        
    nnn = len(groups)
    rep_els = {key: group[0] for key, group in groups.items()}
    
    return rep_els, nnn

