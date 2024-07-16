# Adjacency test - this file tests if the code will produce all the adjacency matrices.

import adjacency as aj

#test
n = 4
adjacency_matrices = aj.all_adj_matrix(n)

for i, matrix in enumerate(adjacency_matrices):
    print(f"Matrix {i+1}:")
    print(matrix)
    print()   
