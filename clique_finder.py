#This file is going to count the degree on each vertex, and then determine if a clique of a certain
# exists within the file.

import numpy as np
import grouping_homomorphics as gh
import adjacency as aj


def find_cliques(n,k, l,adj_mat): #given a list of these
    
    a = gh.group_matrices_by_ones(adj_mat)
    lisst = a[1] #gh returns the keys in the second position
    
    k1 = []
    l1 = []
    
    
    for item in lisst:
        for i in range(n):
            if item[i] == k-1:
                k1.append(item[i])
            else:
                continue
    
    if len(k1) < k:
        #then no clique of size k exists
        print(f'no k-clique found')
    else:
        #a clique of size k does exist
        print(f'K-clique found')
        
    
    for item in lisst:
        for i in range(n):
            if item[i] == l-1:
                l1.append(item[i])
            else:
                continue    
            
    if len(l1) < l:
            #then no clique of size k exists
        print(f'no l-independent set found')
    else:
            #a clique of size k does exist
        print(f'l-independent set found')
    return