#import numpy as np
#import itertools
import networkx as nx #
import matplotlib.pyplot as plt
import math


#make sure to define your matrices as lists of lists, and not numoy arrays.

#note, the drawing function takes in a single matrix, so you need to loop it if you are 
#working with a list of them.

def draw_graph(adj_matrix):
    # Create an empty graph
    n = len(adj_matrix)
    G = nx.Graph()
    # Add nodes
    G.add_nodes_from(range(n))
    # Add edges
    for i in range(n):
        for j in range(i+1, n):
            if adj_matrix[i][j] == 1:
                G.add_edge(i, j, color= 'blue')
            else:
                G.add_edge(i,j, color = 'red')
                
    # Print the graph
    print("Graph:")
    print(G.edges())
    
    pos = {}
    for i in range(n):
        angle = 2 * math.pi * i / n
        pos[i] = (math.cos(angle) + 1) / 2, (math.sin(angle) + 1) / 2
        
                
    edges = G.edges()
    colors = [G[u][v]['color'] for u, v in edges]
    
    # Visualize the graph
    
    nx.draw(G, pos , edge_color = colors , width = 3, with_labels=True)
    plt.title("Graph Visualization")

    #plt.savefig(f'graph1111_{adj_matrix}')
    plt.show()
    plt.clf()
            
    print()
    
    return 




