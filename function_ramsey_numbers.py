# This file must be able to determine the smaller Ramsey numbers
import numpy as np
import function_grouping_homomorphics as gh
import function_bron_kerbosch_clique_finder as bk
import function_matrix_to_edge_connection as mx
import function_complement_graph as cm
import adjacency as aj
import function_drawing as dr
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display, HTML
from io import BytesIO
import Algorithm_outputs_at_each_step_visualisation as ao


def Rams_26_09(k, l):
    k = k
    l = l
    n = 1  # Start the search at 1 nodes and increment until conditions are met.
    all_graphs_meet_condition = False
    
    
    
    if l == 1 or k ==1 :
        all_graphs_meet_condition = True

    while not all_graphs_meet_condition:
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
        
        print(f"for order = {n}")
        
        p1 = len(graphs)
        print(f"Number of graphs to check before removing homomorphic graphs = {p1}")
        
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs1 = gh.count_non_isomorphic_graphs(graphs)
        n_h_graphs = n_h_graphs1[1]  # Homomorphics function returns the matrices and the keys
        
        p2 = len(n_h_graphs)
        print(f"Number of graphs to check after removing homomorphic graphs = {p2}")
        
        print("**************")
        # Step 3: Initialize a list to track which graphs meet the condition
        these_graphs_meet_condition_list = []
        
        # Step 4: Iterate over each graph and check for conditions
        for graph in n_h_graphs:
            
            # Step 5: Find the complement graph for l-set
            complement_graph = cm.complement_graphs(graph)
            
            graph1 = graph
            c_graph1 = complement_graph
            
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
            k_max = max(clique_list_k, key= len)
            l_max = max(clique_list_l, key= len)
            length_k = len(k_max)
            length_l = len(l_max)
            
            
            ##%%%% Visualisation---


            # Construct dataframe with 6 rows and columns for adjacency matrix and image
            df = pd.DataFrame({
                'Adjacency_Matrix': [graph, complement_graph],  # Adjacency matrices
                
                'Graph_Image_1': [dr.draw_graph_1color(graph, "red"), 
                                  dr.draw_graph_1color(complement_graph, "blue")],  # First set of graph images
                
                'Graph_Image_2': [dr.draw_clique_graph(graph, k_max,"red"), 
                                  dr.draw_clique_graph(complement_graph, l_max,"blue")] })


            ao.table_results(df)
            ##%%%%%%
            
            # Step 9: Check if the graph meets at least one condition
            if length_k < k and length_l < l:
                # If neither condition is met, break out of the loop and try a larger graph
                # these_graphs_meet_condition = 0
                graphs = []
                n += 1
                
                break  # Exit the inner loop to restart with a new graph size
            elif length_k >= k or length_l >= l :
                # If the condition is met, mark this graph as successful
                these_graphs_meet_condition_list.append(1)
        
        # If all graphs meet at least one condition, we have found the Ramsey number
        if len(these_graphs_meet_condition_list) == len(n_h_graphs):
            all_graphs_meet_condition = True
        else:
            continue
            
        print("The Ramsey number is =")
    return n


#test
a = Rams_26_09(2, 3)
print(a)