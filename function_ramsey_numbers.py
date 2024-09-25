# This file must be able to determine the smaller Ramsey numbers
import function_adjacency as aj
import function_grouping_homomorphics as gh
import function_bron_kerbosch_clique_finder as bk
import function_matrix_to_edge_connection as mx
import function_drawing as dr
import function_complement_graph as cm
import numpy as np


#%%
def Rams_update(k, l):
    k = k
    l = l
    n = 2  # Start the search at 2 nodes and increment until conditions are met.
    all_graphs_meet_condition = False
    # Base case for k = 2 and l = 2
    if k == 2 and l == 2:
        print("The Ramsey number is 2.")
        return n
    

    while not all_graphs_meet_condition:
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
         
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs1 = gh.group_matrices_by_ones(graphs)
        n_h_graphs = n_h_graphs1[0]  # Homomorphics function returns the matrices and the keys
        
        # Step 3: Initialize a list to track which graphs meet the condition
        these_graphs_meet_condition_list = []
        
        # Step 4: Iterate over each graph and check for conditions
        for graph in n_h_graphs:
            
            #Step 5: Find the complement graph for l-set
            complement_graph = cm.complement_graphs(graph)
            dr.draw_graph(graph)
            # Step 6: Convert to dictionary format for processing
            k_graph = mx.adj_mat_dict(graph)
            l_graph = mx.adj_mat_dict(complement_graph)
            
            # Step 7: Find maximal cliques in both k_graph and l_graph
            clique_set_k = bk.MaximalCliquesFinder(k_graph)
            clique_set_k.find_cliques()
            clique_list_k = clique_set_k.list_of_cliques()
            
            clique_set_l = bk.MaximalCliquesFinder(l_graph)
            clique_set_l.find_cliques()
            clique_list_l = clique_set_l.list_of_cliques()
            
            # Step 8: Find the largest cliques in both k_graph and l_graph
            k_max = max(clique_list_k, key=len)
            length_k = len(k_max)
            
            if length_k == 1:
                k_max=[]
                l_max = list(np.zeros((n,1)))
            
            else:
                l_max = list(np.zeros((n,1))) #complement graph
                l_max = l_max[length_k:]
            
            length_l = len(l_max)
            
            
            print('pair for this graph {graph}')
            k_max = clique_list_k[0]
            l_max = clique_list_l[0]
            
    
            print(k_max)
            print(l_max)
            
            # Step 9: Check if the graph meets at least one condition
            if length_k < k and length_l < l:
                # If neither condition is met, break out of the loop and try a larger graph
                print(f"{n} is not the Ramsey number.")
                these_graphs_meet_condition = 0
                n += 1
                break  # Exit the inner loop to restart with a new graph size
            else:
                # If the condition is met, mark this graph as successful
                these_graphs_meet_condition_list.append(graph)
        
        # If all graphs met at least one condition, we have found the Ramsey number
        if len(these_graphs_meet_condition_list) == len(n_h_graphs):
            all_graphs_meet_condition = True
            print(f"The Ramsey number is {n}.")
        else:
            continue
            
    return n
            
# Test the function
k = 3
l = 2
p = Rams_update(k, l)
print(p)

#%%
for i in range(5):
    if i == 2:
        break  # Exit the loop when i == 2
    print(f"i: {i}")
print("Loop is finished.")



