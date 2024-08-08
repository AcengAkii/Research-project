#This file is going to count the degree on each vertex, and then determine if a clique of a certain
# exists within the file.
import grouping_homomorphics as gh
import drawing as dr
import numpy as np
import complement_graph as cg
#n - nodes, k- k-cliques, l-lindep sets
def find_cliques(n,k, l,adj_mat): #given a list of adjacency matrices
    k1 = [] 
    l1 = []  #list to store nodes with high enough degrees to make a clique 
    pmk =[]
    pml = [] #list to store matrices with possible cliques
    a = gh.group_matrices_by_ones(adj_mat)
    lisst = a[1] #gh[1] returns the degree on each node per row (in blue)
    lisst2 = []
    l_list = a[1]
    
    
    admlist = a[0] #adjacency matrix list
    
###################################      1      ##############################################
    for item in l_list: #edge sequences for the complementary graphs.
        temp_list = list(item)
        for i in range(len(temp_list)):
            temp_list[i] = n - 1 - temp_list[i]
        lisst2.append(tuple(temp_list))
            
###################################      2      ##############################################

    for item in lisst:
        for i in range(n):
            if item[i] == k-1: #you must have k-1 edges per node and k nodes to have a complete graph
                k1.append(item[i])
            else:
                continue

        if len(k1) < k:
            #then no clique of size k exists
            print('no k-clique found in {}', item)
            dr.draw_graph_1color(admlist[item])
        else:
            #a clique of size k might exist
            #now store the matrix in pmk
            pmk.append(item)
            print('possible K-clique exists in {}', item)
            dr.draw_graph_1color(admlist[item])
        k1 = []
            
    print()
    print()
            
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
            print('no l-independent set found in {}', item)
        else:
            #a clique of size k does exist
            #now store that matrix in pml
            pml.append(item)
            print('possible l-independent set in {}', item)
        
###################################      4      ##############################################
        
    if len(k1)<k and len(l1)<l: #neither exist
        print("increase the size of the graph")
    else:
        print('This graph my have eithe k or l no matter how you draw it')
    l1 = []
        
###################################      5      ##############################################

    #convert the keys in each list into a matrix to make it easier to work with later
    
        
    return pml, pmk


############
############
############

def find_cliques2(k,l,adj_mat):
    k1 = [] 
    l1 = []  #list to store nodes with high enough degrees to make a clique 
    pmk =[]
    pml = [] #list to store matrices with possible cliques
    a = gh.group_matrices_by_ones(adj_mat)
    a = list(a)
    n = len(a[0][0])
    m = len(a[1])
    
    lisst = a[1] #gh[1] returns the degree on each node per row (in blue)
    lisst2 = []
    l_list = a[1]
    l2 = []
    cmg = []
    
    admlist = a[0] #adjacency matrix list
            
    
    for p in range(m):
        for i in range(n):
            if a[1][p][i] >= k-1  : #you must have k-1 edges per node and k nodes to have a complete graph
                k1.append(a[1][p][i])
            else:
                continue

        if len(k1) < k:
            #then no clique of size k exists
            print('no' ,k,'-clique found in', a[1][p])
        else:
            #a clique of size k might exist
            #now store the matrix in pmk
            pmk.append(a[1][p])
            print('possible',k,'-clique exists in {}', a[1][p])
            
           
        k1 = []
        
    #     print(np.array(a[0][p]))
    #     dr.draw_graph_1color(a[0][p])
    #     print('*************************', k)
        
    # print()
    # print()
            
###################################      3      ##############################################
    #repeat for l-indep set    
    #making the complement graphs
    for item in admlist:
        graph_matrix = cg.complement_graphs(item)
        edge_seq = gh.ones_per_row(graph_matrix)
        
        cm = [graph_matrix,edge_seq]
        cmg.append(cm)
            

    for q in range(m):
        for i in range(n):
            if cmg[q][1][i] >= l-1:
                l1.append(cmg[q][1][i])
            else:
                continue    
            
        if len(l1) < l:
            #then no clique of size k exists
            print('no' ,l,'-independent set found in {}', item)
        else:
            #a clique of size k does exist
            #now store that matrix in pml
            pml.append(cmg[q][0])
            print('possible' ,l,'-independent set in {}', item)
            
        # print(np.array(cmg[q][0]))
        # dr.draw_graph_1color(cmg[q][0])
        # print('*************************')
            
        # print()
        # print()
        
###################################      4      ##############################################
    print('*************************')
    
    if len(k1)<k and len(l1)<l: #neither exist
        print("increase the size of the graph")
    else:
        print('This graph my have eithe k or l no matter how you draw it')

###################################      5      ##############################################
    
        
    return pml, pmk



#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################

#######################################################################################


def find_cliques3(k,l,adj_mat):
    k1 = [] 
    l1 = []  #list to store nodes with high enough degrees to make a clique 
    pmk =[]
    pml = [] #list to store matrices with possible cliques
    a = gh.group_matrices_by_ones(adj_mat)
    a = list(a)
    n = len(a[0][0])
    m = len(a[1])
    
    cmg = []
    
    admlist = a[0] #adjacency matrix list
    #making the complement graphs
    for item in admlist:
        graph_matrix = cg.complement_graphs(item)
        edge_seq = gh.ones_per_row(graph_matrix)
        
        cm = [graph_matrix,edge_seq]
        cmg.append(cm)
            
    
    for p in range(m):
        found_clique_or_independent_set = False
        for i in range(n):
            if a[1][p][i] >= k-1  : #you must have k-1 edges per node and k nodes to have a complete graph
                k1.append(a[1][p][i])
            else:
                continue
        

        if len(k1) < k:
            #then no clique of size k exists
            print('no' ,k,'-clique found in', a[1][p])
        else:
            #a clique of size k might exist
            #now store the matrix in pmk
            pmk.append(a[1][p])
            found_clique_or_independent_set = True
            print('possible',k,'-clique exists in {}', a[1][p])
            
           
        k1 = []
        
        print(np.array(a[0][p]))
        dr.draw_graph_1color(a[0][p])
        
        print()
        print()
            

        if cmg[p][1][i] >= l-1:
            l1.append(cmg[p][1][i])
        else:
            continue    
            
        if len(l1) < l:
            #then no clique of size k exists
            print('no' ,l,'-independent set found in {}', item)
        else:
            #a clique of size k does exist
            #now store that matrix in pml
            pml.append(cmg[p][0])
            found_clique_or_independent_set = True
            print('possible' ,l,'-independent set in {}', item)
        l1 = []
        
        if not found_clique_or_independent_set:
            print("Increase the size of the graph")
            return pml, pmk
        
        
        print(np.array(cmg[p][0]))
        dr.draw_graph_1color(cmg[p][0])
        print('*************************')
            
        print()
        print()
        
###################################      4      ##############################################
        
    if len(k1)<k and len(l1)<l: #neither exist
        print("increase the size of the graph") #this condition is not correct, i need to change it
        #to have a pairwise comparison
        #use a boolean to compare valuse and you should get the ramsey number out
        #assign each of those valuse 1 or 2 and then if one of the conditions is met for all graphs 
        #youve found your ramsey number.
    else:
        print('This graph my have eithe k or l no matter how you draw it')

###################################      5      ##############################################
    
        
    return pml, pmk


def find_cliques4(k, l, adj_mat):
    k1 = [] 
    l1 = []  # list to store nodes with high enough degrees to make a clique 
    pmk = []
    pml = [] # list to store matrices with possible cliques
    a = gh.group_matrices_by_ones(adj_mat)
    a = list(a)
    n = len(a[0][0])
    m = len(a[1])
    
    cmg = []
    
    admlist = a[0] # adjacency matrix list
    # making the complement graphs
    for item in admlist:
        graph_matrix = cg.complement_graphs(item)
        edge_seq = gh.ones_per_row(graph_matrix)
        
        cm = [graph_matrix, edge_seq]
        cmg.append(cm)
    
    for p in range(m):
        found_clique_or_independent_set = False  # Flag to check if a k-clique or l-set is found
        
        # Check for k-clique
        for i in range(n):
            if a[1][p][i] >= k-1:
                k1.append(a[1][p][i])
            else:
                continue
        
        if len(k1) < k:
            # No clique of size k exists
            print('No', k, '-clique found in', a[1][p])
        else:
            # A clique of size k might exist
            pmk.append(a[1][p])
            print('Possible', k, '-clique exists in', a[1][p])
            found_clique_or_independent_set = True
        
        k1 = []
        
        print(np.array(a[0][p]))
        dr.draw_graph_1color(a[0][p])
        print()
        print()
        
        # Check for l-set in the complementary graph
        for i in range(n):
            if cmg[p][1][i] >= l-1:
                l1.append(cmg[p][1][i])
            else:
                continue
        
        if len(l1) < l:
            # No independent set of size l exists
            print('No', l, '-independent set found in', cmg[p][0])
        else:
            # An independent set of size l might exist
            pml.append(cmg[p][0])
            print('Possible', l, '-independent set in', cmg[p][0])
            found_clique_or_independent_set = True
        
        l1 = []
        
        print(np.array(cmg[p][0]))
        dr.draw_graph_1color(cmg[p][0])
        print('*************************')
        print()
        print()
        
        if not found_clique_or_independent_set:
            print("Increase the size of the graph")
            return pml, pmk

    print('This graph may have either k-cliques or l-independent sets no matter how you draw it')
    return pml, pmk







