import function_clique_finder as cf
import function_grouping_homomorphics as gh
import function_adjacency as aj
import function_drawing as dr

#step 1- define vars
n = 4
k = 2
l = 2
#step 2 - get adj_matrices
adjm_list = aj.all_adj_matrix(n)
#adjm_list2 = gh.group_matrices_by_ones(adjm_list)

#result = cf.find_cliques(n, k, l, adjm_list)

result2 = cf.find_cliques5(k, l, adjm_list)

