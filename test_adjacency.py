# Adjacency test - this file tests if the code will produce all the adjacency matrices.

import adjacency as aj
import function_grouping_homomorphics as gh
import function_drawing as dr

# test
n = 4
adjacency_matrices = aj.all_adj_matrix(n)

for i, matrix in enumerate(adjacency_matrices):
	print(f"Matrix {i+1}:")
	print(matrix)
	print("\n")   

A = gh.group_matrices_by_ones(adjacency_matrices)
print(A)
print("\n")   


for matrix in A[0]:
	print(matrix)
	print(len(matrix))
	print("\n")   
	dr.draw_graph(matrix)

