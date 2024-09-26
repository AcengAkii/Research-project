#import numpy as np
#import itertools
import networkx as nx #
import matplotlib.pyplot as plt
import math

import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

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
                G.add_edge(i, j, color= 'red')
            else:
                G.add_edge(i,j, color = 'blue')
                
    # Print the graph
    print("Graph:")
    print(G.edges())


    
    pos = {}
    for i in range(n):
        angle = 2 * math.pi * i / n
        pos[i] = (math.cos(angle) + 1) / 2, (math.sin(angle) + 1) / 2

    edges = G.edges()
    colors = [G[u][v]['color'] for u, v in edges]

    nx.draw(G, pos , edge_color = colors , width = 3, with_labels=True)
    plt.title("Graph Visualization")
    plt.figtext(0,0,"blue = indep set ; red=clique")


    nx.draw(G, pos , edge_color = colors , width = 3, with_labels=True)

    plt.title("Graph Visualization")

    #plt.savefig(f'graph1111_{adj_matrix}')
    plt.show()
    plt.clf()
        
    print()

    return 


def draw_graph_1color(adj_matrix, colour):
    # Create an empty graph
    n = len(adj_matrix)
    G = nx.Graph()
    G2 = nx.Graph()
    
    # Add nodes
    G.add_nodes_from(range(n))
    G2.add_nodes_from(range(n))
    
    # Add edges for the first graph (G)
    for i in range(n):
        for j in range(i+1, n):
            if adj_matrix[i][j] == 1:
                G.add_edge(i, j)
                
    # Add edges for the second graph (G2) - this creates a complete graph of non-connections
    for p in range(n):
        for q in range(p+1, n):
            if adj_matrix[p][q] == 0:
                G2.add_edge(p, q)
    
    # Position nodes in a circular layout
    pos = {}
    for i in range(n):
        angle = 2 * math.pi * i / n
        pos[i] = (math.cos(angle), math.sin(angle))
        
    # Print the graph edges (optional)
    print("Graph edges:", G.edges())
    
    # Visualize the graph
    nx.draw(G, pos, edge_color=colour, width=3, with_labels=True)  # Corrected color usage
    plt.title("Graph Visualization")
    
    #plt.show()
    #plt.clf()
    
    
    # Convert the plot to an image
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    img = Image.open(buf)
    return img


def draw_clique_graph(adj_matrix, clique_nodes,colour):
    # Create graph and add all nodes
    G = nx.Graph()
    n = len(adj_matrix)
    G.add_nodes_from(range(n))  # Add all nodes to the graph

    # Add edges for the clique
    G.add_edges_from((i, j) for i in clique_nodes for j in clique_nodes if adj_matrix[i][j])


    # Position nodes in a circular layout
    pos = {}
    for i in range(n):
        angle = 2 * math.pi * i / n
        pos[i] = (math.cos(angle), math.sin(angle))
        
        
    # Draw the entire graph with all nodes
    nx.draw(G, pos, edge_color='lightgray', width=1, with_labels=True)

    # Highlight the clique edges in red
    clique_edges = [(i, j) for i in clique_nodes for j in clique_nodes if adj_matrix[i][j]]
    nx.draw_networkx_edges(G, pos, edgelist=clique_edges, edge_color=colour, width=3)

    plt.title("Clique Graph Visualization")
    plt.axis('equal')  # Equal aspect ratio ensures that circles look circular.
    #plt.show()
    
    # Convert the plot to an image
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    img = Image.open(buf)   
    return img

