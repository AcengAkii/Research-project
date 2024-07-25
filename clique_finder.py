#This file is going to count the degree on each vertex, and then determine if a clique of a certain
# exists within the file.
import grouping_homomorphics as gh


#n - nodes, k- k-cliques, l-lindep sets
def find_cliques(n,k, l,adj_mat): #given a list of adjacency matrices
    k1 = [], l1 = []  #list to store nodes with high enough degrees to make a clique 
    pmk =[], pml = [] #list to store matrices with possible cliques
    a = gh.group_matrices_by_ones(adj_mat)
    lisst = a[1] #gh[1] returns the degree on each node per row (in blue)
    lisst2 = a[1]
    
###################################      1      ##############################################
    for item in lisst2: #edge sequences for the complementary graphs.
        for i in range(n):
            item[i] = n - item[i]
            
###################################      2      ##############################################

    for item in lisst:
        for i in range(n):
            if item[i] == k-1: #you must have k-1 edges per node and k nodes to have a complete graph
                k1.append(item[i])
            else:
                continue
    
        if len(k1) < k:
            #then no clique of size k exists
            print('no k-clique found')
        else:
            #a clique of size k might exist
            #now store the matrix in pmk
            pmk.append(item)
            print('possible K-clique exists')
            
###################################      3      ##############################################

    #repeat for l-indep set
    for item in lisst2:
        for i in range(n):
            if item[i] == l-1:
                l1.append(item[i])
            else:
                continue    
            
        if len(l1) < l:
            #then no clique of size k exists
            print('no l-independent set found')
        else:
            #a clique of size k does exist
            #now store that matrix in pml
            pml.append(item)
            print('possible l-independent set')
        
###################################      4      ##############################################
        
    if len(k1)<k and len(l1)<l: #neither exist
        print("increase the size of the graph")
    else:
        print('Now go check each graph for what does exist')
        
###################################      5      ##############################################

    #convert the keys in each list into a matrix to make it easier to work with later
    
        
    return pml, pmk



















