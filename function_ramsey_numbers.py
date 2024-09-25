# This file must be able to determine the smaller Ramsey numbers
import numpy as np
import function_grouping_homomorphics as gh
import function_bron_kerbosch_clique_finder as bk
import function_matrix_to_edge_connection as mx
import function_complement_graph as cm
import function_adjacency1 as aj
import function_drawing as dr
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display, HTML
from io import BytesIO


#%%
def Rams(k,l):
    
    n = 2 #we start pur search at 2 nodes and will keep incrementing 
    #until our conditions are met.
    
    clique_exists = True #initialization
    l_set_exists = True #initialization

    #step 1 : Build the adjacency matrices
    graphs =  aj.all_adj_matrix(n)
    #step 2: find all the non-homomorphic graphs
    n_h_graphs = gh.group_matrices_by_ones(graphs)

    #step3: convert the graphs to a dictionary
    n_h_graphs = mx.adj_mat_dict(n_h_graphs)
    
  
    # step 4: Find the k-cliques that appear in each graph:
    for graph in n_h_graphs:
        
        #wrapping it all in  a while loop: i.e while anything but false false conduct the search
        #and if we find false false increas n by 1 and start again.
    
        clique_set = bk.MaximalCliquesFinder(graph)
        clique_set.find_cliques()
        
        clique_list = clique_set.list_of_cliques()
        u = len(clique_list)
        #now take the clique of the biggest size: say it returns a list of cliques
        for p in range(u):
            
            length = len(clique_list[p])
            if  length < k:
                #k clique not found
                clique_exists = False
                
            elif length < l:
                #l set not found
                l_set_exists = False
                
            elif length >= k:
                #k clique found
                clique_exists = True
                
            elif length >= l: 
                #l set found
                l_set_exists = True
                    
            #now that we have what we need - check if either k/l exist (i.e are true)
            #if at any point, both are false then we must increase the number 
            #of nodes and start the process again
            if clique_exists == False and l_set_exists == False:
                n = n+1
                break # I want to break the while loop at this point and start again at a higher number of n
            
            else: #anything else requires us to continue with the check.
                continue
            
            
            
            #if it doesnt break at anypoint - youve found your Ramsey number and we want to 
            # and we must print that number n
            
    print("The Ramsey number is")
    print(n)
    
    return n



def Rams_2(k, l):
    
    n = 2   # We start our search at 2 nodes and will keep incrementing until our conditions are met.

    while True:  # Infinite loop that will only break when the correct conditions are met.
        clique_exists = True  # Initialization
        l_set_exists = True  # Initialization

        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs = gh.group_matrices_by_ones(graphs)
        n_h_graphs = n_h_graphs[0] #homomorphics function returns the matrices and the keys
        # Step 3: Convert the graphs to a dictionary
        new = []
        for item in n_h_graphs:
            n_h_dict = mx.adj_mat_dict(item)
            new.append(n_h_dict)
    
        # Step 4: Find the k-cliques that appear in each graph:
        for graph in new:
            
            clique_set = bk.MaximalCliquesFinder(graph)
            clique_set.find_cliques()
            clique_list = clique_set.list_of_cliques()
            
            u = len(clique_list)

            # Reset the flags before checking each graph
            clique_exists = False
            l_set_exists = False

            # Now take the clique of the biggest size: say it returns a list of cliques
            for p in range(u):
                length = len(clique_list[p])
                
                if length >= k:
                    clique_exists = True
                
                if length >= l:
                    l_set_exists = True
                
                # If both conditions are met, we can exit early for this graph
                if clique_exists and l_set_exists:
                    break
            
            # If either condition is not met, we need to increase n and restart
            if not clique_exists or not l_set_exists:
                n += 1
                break  # Exit the for loop to start the process again with a higher n
            
        # If we have checked all graphs and both conditions are met, we've found our Ramsey number
        if clique_exists | l_set_exists:
            print("The Ramsey number is")
            print(n)
        
        return n


def Rams_3(k, l):
    
    n = 2  # Start the search at 2 nodes and increment until conditions are met.
    all_graphs_meet_condition = False
    
    while  all_graphs_meet_condition == False:  # Infinite loop that continues until the condition is met for all graphs.
         # Assume all graphs meet the conditions initially
        stp = []
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs = gh.group_matrices_by_ones(graphs)
        n_h_graphs = n_h_graphs[0]  # Homomorphics function returns the matrices and the keys
        # Step 3: Convert the graphs to a dictionary
        new = []
        
        for item in n_h_graphs:
            n_h_dict = mx.adj_mat_dict(item)
            new.append(n_h_dict)
    
        # Step 4: Find the k-cliques and l_sets that appear in each graph:
        for graph in new:
            clique_set = bk.MaximalCliquesFinder(graph)
            clique_set.find_cliques()
            clique_list = clique_set.list_of_cliques()
            
            u = len(clique_list)

            clique_exists = True
            l_set_exists = True

            # Check each clique to see if it meets the conditions
            for p in range(u):
                length = len(clique_list[p])
                
                if length >= k:
                    clique_exists = True
                
                if length >= l:
                    l_set_exists = True

                # If at least one condition is met, stop checking this graph
                if clique_exists == True or l_set_exists == True:
                    a = 1 
                    stp.append(a)
                    continue
        if len(stp) < len(n_h_graphs):
            all_graphs_meet_condition = False
            # Increment n and try again
            n += 1
        
        else:
            all_graphs_meet_condition == True
            print("The Ramsey number is")
            break

    return n





def Rams_4(k, l):
    
    n = 2  # Start the search at 2 nodes and increment until conditions are met.
    all_graphs_meet_condition = False
    
    while all_graphs_meet_condition == False:  # Loop continues until condition is met for all graphs
        stp = []
        
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
        
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs = gh.group_matrices_by_ones(graphs)
        n_h_graphs = n_h_graphs[0]  # Homomorphics function returns the matrices and the keys
        
        # Step 3: Convert the graphs to a dictionary
        new = []
        for item in n_h_graphs:
            n_h_dict = mx.adj_mat_dict(item)
            new.append(n_h_dict)
            
        clique_exists = False
        l_set_exists = False
        # Step 4: Find the k-cliques and l_sets that appear in each graph:
        for graph in new:
            clique_set = bk.MaximalCliquesFinder(graph)
            clique_set.find_cliques()
            clique_list = clique_set.list_of_cliques()
            

            # Find the max clique
            b = max(clique_list, key=len)
            length = len(b)
            
            if length >= k:
                clique_exists = True
                
            if length >= l:
                l_set_exists = True

            # If at least one condition is met, stop checking this graph
            if clique_exists == True or l_set_exists == True:
                stp.append(1)
        
        # If every graph in the current set met at least one condition, stop the loop
        if len(stp) >= len(n_h_graphs):
            all_graphs_meet_condition = True
            print("The Ramsey number is", n)
            
        else:
            print(n, 'is not the ramsey number')
            n += 1

    return n



def Rams_5(k, l):
    n = 2  # Start the search at 2 nodes and increment until conditions are met.
    
    while True:  # Infinite loop that continues until the condition is met for all graphs.
        stp = []
        print(f"Checking n = {n}")  # Debugging print to track iterations
        
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
        
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs = gh.group_matrices_by_ones(graphs)
        n_h_graphs = n_h_graphs[0]  # Homomorphics function returns the matrices and the keys
        
        # Step 3: Convert the graphs to a dictionary
        new = []
        for item in n_h_graphs:
            n_h_dict = mx.adj_mat_dict(item)
            new.append(n_h_dict)
    
        # Step 4: Find the k-cliques and l_sets that appear in each graph:
        for graph in new:
            clique_set = bk.MaximalCliquesFinder(graph)
            clique_set.find_cliques()
            clique_list = clique_set.list_of_cliques()
            
            clique_exists = False
            l_set_exists = False

            # Find the max clique
            if clique_list:
                b = max(clique_list, key=len)
                length = len(b)
            else:
                length = 0  # Handle cases with no cliques found
            
            if length >= k:
                clique_exists = True
                
            if length >= l:
                l_set_exists = True

            # If at least one condition is met, add to `stp`
            if clique_exists == True or l_set_exists == True:
                stp.append(1)

        # Check if all graphs met the condition
        if len(stp) == len(n_h_graphs):
            print("The Ramsey number is", n)
            break  # Exit the while loop since all graphs met at least one condition
            
        else:
            print(n, 'is not the ramsey number')
        
            n += 1  # Increment n and try again

    return n




#i added the complementary graph analysis here...
def Rams_comp(k, l):
    
    n = 2  # Start the search at 2 nodes and increment until conditions are met.
    all_graphs_meet_condition = False
    # Initialize conditions for each round
    clique_exists = False
    l_set_exists = False

    while all_graphs_meet_condition == False:  # Loop continues until condition is met for all graphs
        
        stop = []
        
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
        
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs = gh.group_matrices_by_ones(graphs)
        n_h_graphs = n_h_graphs[0]  # Homomorphics function returns the matrices and the keys
        
        all_graphs = len(n_h_graphs)

        
        # Step 4: Find the k-cliques and l_sets that appear in each graph:
        for graph in n_h_graphs:
            
            #find the l-set
            new = cm.complement_graphs(graph)
            #convert to dicts
            k_graph = mx.adj_mat_dict(graph)
            l_graph = mx.adj_mat_dict(new)
            
            #for the cliques
            clique_set = bk.MaximalCliquesFinder(k_graph)
            clique_set.find_cliques()
            clique_list = clique_set.list_of_cliques()
            
            #for the sets
            clique_set_l = bk.MaximalCliquesFinder(l_graph)
            clique_set_l.find_cliques()
            clique_list_l = clique_set_l.list_of_cliques()
            

            # Find the max clique
            k_max = max(clique_list, key=len)
            l_max = max(clique_list_l, key=len)
            
            
            length_k = len(k_max)
            length_l = len(l_max)
            
            
            if length_k >= k:
                clique_exists = True
            else: 
                clique_exists = False
                
            if length_l >= l:
                l_set_exists = True
            else: 
                l_set_exists = False
                
            # If at least one condition is met, stop checking this graph
            if clique_exists == False and l_set_exists == False:
                break
            else:
                stop.append(1)
                
        
        # If every graph in the current set met at least one condition, stop the loop
        if len(stop) >= all_graphs:  # Ensure we are comparing against the correct length
            all_graphs_meet_condition = True
            print("The Ramsey number is", n)
        else:
            all_graphs_meet_condition = False
            print(n, 'is not the Ramsey number')
            n += 1  # Increment n and try again

    return n

#%%

def Rams_comp33(k, l):
    n = 2  # Start the search at 2 nodes and increment until conditions are met.
    all_graphs_meet_condition = False

    while not all_graphs_meet_condition:
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
         
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs1 = gh.group_matrices_by_ones(graphs)
        n_h_graphs = n_h_graphs1[0]  # Homomorphics function returns the matrices and the keys
        
        # Step 3: Initialize a list to track which graphs meet the condition
        these_graphs_meet_condition = []
        
        # Step 4: Iterate over each graph and check for conditions
        for graph in n_h_graphs:
            
            # Step 5: Find the complement graph for l-set
            complement_graph = cm.complement_graphs1(graph)
            
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
            l_max = max(clique_list_l, key=len)
            
            length_k = len(k_max)
            length_l = len(l_max)
            
            # Step 9: Check if the graph meets at least one condition
            if length_k < k and length_l < l:
                # If neither condition is met, break out of the loop and try a larger graph
                print(f"{n} is not the Ramsey number.")
                n += 1
                break  # Exit the inner loop to restart with a new graph size
            else:
                # If the condition is met, mark this graph as successful
                these_graphs_meet_condition.append(1)
        
        # If all graphs met at least one condition, we have found the Ramsey number
        if len(these_graphs_meet_condition) == len(n_h_graphs):
            all_graphs_meet_condition = True
            print(f"The Ramsey number is {n}.")
            
    return n
            
# # Test the function
# k = 2
# l = 2
# p = Rams_comp33(k, l)
# print(p)



# %%
def Rams_comp3(k, l):
    n = 2  # Start the search at 2 nodes and increment until conditions are met.
    all_graphs_meet_condition = 0

    while all_graphs_meet_condition == 0:
          
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
         
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs1 = gh.group_matrices_by_ones(graphs)
        n_h_graphs = n_h_graphs1[0]  # Homomorphics function returns the matrices and the keys
        
        # Step 3: Initialize a flag to check if all graphs meet the condition
        #all_graphs_meet_condition = True  # Assume all graphs will meet the condition
        these_graphs_meet_condition_list = []
        # Step 4: Iterate over each graph and check for conditions
        for graph in n_h_graphs:
            
            # Step 5: Find the complement graph for l-set
            complement_graph = cm.complement_graphs1(graph)
            
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
            # k_max = max(clique_list_k, key=len)
            # l_max = max(clique_list_l, key=len)
            
            k_max = clique_list_k[0]
            l_max = clique_list_l[0]
            
            length_k = len(k_max)
            length_l = len(l_max)
            
           # Step 9: Check if the graph meets at least one condition
            if length_k < k and length_l < l:
                # If neither condition is met, break out of the loop and try a larger graph
                these_graphs_meet_condition = 0 #0-false
                print(f"{n} is not the Ramsey number.")
                n += 1
                break  # Exit the inner loop to restart with a new graph size
            
            else:
                these_graphs_meet_condition = 1 #1 is true
                these_graphs_meet_condition_list.append(1)
    # If all graphs met at least one condition, we have found the Ramsey number
        if len(these_graphs_meet_condition) == len(n_h_graphs1):
            print(f"The Ramsey number is {n}.")
            
    return n
            
# # Test the function
# k = 2
# l = 2
# p = Rams_comp3(k, l)
# print(p)


#%%
def Rams_comp_update1(k, l):
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
            
            # Step 5: Find the complement graph for l-set
            complement_graph = cm.complement_graphs(graph)
            
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
            
            # if length_k == 1:
            #     k_max=[]
            #     l_max = list(np.zeros((n,1)))
            
            # else:
            #     l_max = list(np.zeros((n,1))) #complement graph
            #     l_max = l_max[length_k:]
            
            # length_l = len(l_max)
            
            
            # print('pair for this graph {graph}')
            # print('non-homomorphic graph data')
            # print("max k-clique in this graph is of size", length_k,' and is made of the following vertices:')
            # print(k_max)
    
            # print('max l-independent set in this graph is of size', length_l,'and is made of the following vertices:')
            # print(l_max)
        
            print('***************************************************************************')
            
            # Create data
            data = {
                'size of graph': [n],
                'max k-clique': [k_max],
                'max l-independent set': [l_max] }
            
            pic = dr.draw_graph(graph)
            graph_buffer = draw_graph_in_memory(graph)
            
            df = pd.DataFrame(data)
            
            # Display the figure and table side by side using HTML
            display(HTML(f"""
            <div style="display: flex; align-items: center;">
                <div style="flex: 1;">
                    <img src=" graph_buffer " width="250">
                </div>
                <div style="flex: 1;">
                    {df.to_html(index=False)}
                </div>
            </div>
            """))

            # Step 9: Check if the graph meets at least one condition
            if length_k < k and length_l < l:
                # If neither condition is met, break out of the loop and try a larger graph
                print(f"{n} is not the Ramsey number.")
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
            print(f"The Ramsey number is {n}.")
            print()
            print()
        else:
            continue
            
    return n
            

#%%
def Rams_comp_update2(k, l):
    k = k
    l = l
    n = 1  # Start the search at 2 nodes and increment until conditions are met.
    all_graphs_meet_condition = False
    # Base case for k = 2 and l = 2
    # if k == 2 and l == 2:
    #     print("The Ramsey number is 2.")
    #     return n
    if l == 1 or k ==1 :
        all_graphs_meet_condition = True

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
            
            # Step 5: Find the complement graph for l-set
            complement_graph = cm.complement_graphs(graph)
            
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
            
    return n

#%%
def draw_graph_in_memory(graph):
    fig, ax = dr.draw_graph(graph)  # Your function that draws the graph
    buf = BytesIO()
    fig.savefig(buf, format='png')  # Save the figure to the in-memory buffer
    buf.seek(0)  # Rewind the buffer to the beginning so it can be read
    plt.close(fig)  # Close the figure to free memory
    return buf

#%%
def Rams_comp_update3(k, l):
    k = k
    l = l
    n = 1  # Start the search at 1 nodes and increment until conditions are met.
    all_graphs_meet_condition = False
    # Base case for k = 2 and l = 2
    # if k == 2 and l == 2:
    #     print("The Ramsey number is 2.")
    #     return n
    if l == 1 or k ==1 :
        all_graphs_meet_condition = True

    while not all_graphs_meet_condition:
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
         
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs1 = gh.count_non_isomorphic_graphs(graphs)
        n_h_graphs = n_h_graphs1[1]  # Homomorphics function returns the matrices and the keys
        
        # Step 3: Initialize a list to track which graphs meet the condition
        these_graphs_meet_condition_list = []
        
        # Step 4: Iterate over each graph and check for conditions
        for graph in n_h_graphs:
            
            # Step 5: Find the complement graph for l-set
            complement_graph = cm.complement_graphs(graph)
            
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
            
    return n

#%%
def Rams_comp_update3_print(k, l):
    k = k
    l = l
    n = 1  # Start the search at 1 nodes and increment until conditions are met.
    all_graphs_meet_condition = False
    # Base case for k = 2 and l = 2
    # if k == 2 and l == 2:
    #     print("The Ramsey number is 2.")
    #     return n
    if l == 1 or k ==1 :
        all_graphs_meet_condition = True

    while not all_graphs_meet_condition:
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
         
        # Step 2: Find all the non-homomorphic graphs
        n_h_graphs1 = gh.count_non_isomorphic_graphs(graphs)
        n_h_graphs = n_h_graphs1[1]  # Homomorphics function returns the matrices and the keys
        
        # Step 3: Initialize a list to track which graphs meet the condition
        these_graphs_meet_condition_list = []
        
        # Step 4: Iterate over each graph and check for conditions
        for graph in n_h_graphs:
            
            # Step 5: Find the complement graph for l-set
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
            k_max = max(clique_list_k, key= len)
            l_max = max(clique_list_l, key= len)
            length_k = len(k_max)
            length_l = len(l_max)
            
            
            
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
            
    return n