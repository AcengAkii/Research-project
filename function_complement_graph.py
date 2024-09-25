# making complement graphs:
    
# I want a list of rows and columns where the first column is the edge sequences and 
# the second row is the 
import numpy as np

#pass through a single adjacency matrics
def complement_graphs(adj_mat):
    #make the ones zeros and the zeros ones
    
    n = len(adj_mat)
    a = np.zeros((n,n)).tolist()
    
    for i in range(n):
        for j in range(n):
            if i != j:
                if adj_mat[i][j] == 1:
                    a[i][j] = 0
                elif adj_mat[i][j] == 0:
                    a[i][j] = 1
            else:
                a[i][j] = 0
                
    return a


def complement_graphs1(adj_mat):
    # Make the ones zeros and the zeros ones, excluding the diagonal elements
    n = len(adj_mat)
    for i in range(n):
        for j in range(n):
            if i != j:  # Check if the current element is not on the diagonal
                adj_mat[i][j] = abs(1-adj_mat[i][j])
    return adj_mat