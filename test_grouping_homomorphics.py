#Test the function for grouping the matrices
import grouping_homomorphics as gh
import drawing as dr

#Test it out FOR N = 3
A = [[0,0,0],[0,0,0],[0,0,0]]
B = [[0,1,0],[1,0,0],[0,0,0]]
C = [[0,1,1],[1,0,0],[1,0,0]]
D = [[0,1,0],[1,0,1],[0,1,0]]
E = [[0,0,0],[0,0,1],[0,1,0]]
F = [[0,0,1],[0,0,0],[1,0,0]]
G = [[0,0,1],[1,0,1],[1,0,0]] 
H = [[0,1,1],[1,0,1],[1,1,0]]

all_matrices = [A,B,C,D,E,F,G,H]

test_gh = gh.group_matrices_by_ones(all_matrices)


#Test for N=4 
