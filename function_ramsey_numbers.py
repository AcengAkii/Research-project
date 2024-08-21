# This file must be able to determine the smaller Ramsey numbers
import function_adjacency as aj
import function_grouping_homomorphics as gh
import function_bron_kerbosch_clique_finder as bk
import function_matrix_to_edge_connection as mx

def Rams(k,l):
    n = 2 #we start pur search at 2 nodes and will keep incrementing 
    #until our conditions are met.
    
    clique_exists = True #initialization
    l_set_exists = True #initialization
    
    #wrapping it all in  a while loop: i.e while anything but false false conduct the search
    #and if we find false false increas n by 1 and start again.
    while clique_exists == True | l_set_exists == True:
    
        #step 1 : Build the adjacency matrices
        graphs =  aj.all_adj_matrix(n)
        #step 2: find all the non-homomorphic graphs
        n_h_graphs = gh.group_matrices_by_ones(graphs)
    
        #step3: convert the graphs to a dictionary
        n_h_graphs = mx.adj_mat_dict(n_h_graphs)
      
        #step 4: Find the k-cliques that appear in each graph:
        for graph in n_h_graphs:
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
            if clique_exists == False , l_set_exists == False:
                n = n+1
                break # I want to break the while loop at this point and start again
            
            else: #anything else requires us to continue with the check.
                continue
            
            #if it doesnt break at anypoint - youve found your Ramsey nu,ber and we want to 
            # and we must print that number n
            
    
    
    
    return n