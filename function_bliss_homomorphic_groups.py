"""
Bliss Homomorphics function 
"""
import function_adjacency as aj
import networkx as nx
# import pybliss

# def are_isomorphic(graph1, graph2):
#     """
#     Check if two graphs are isomorphic using the canonical form from pybliss.

#     Args:
#         graph1 (pybliss.Graph): First graph.
#         graph2 (pybliss.Graph): Second graph.

#     Returns:
#         bool: True if the graphs are isomorphic, False otherwise.
#     """
#     return graph1.canonical_form() == graph2.canonical_form()

# def find_unique_non_isomorphic_graphs(adjacency_matrices):
#     """
#     Find unique non-isomorphic graphs from a list of adjacency matrices.

#     Args:
#         adjacency_matrices (list of lists): A list of adjacency matrices representing graphs.

#     Returns:
#         int: Number of unique non-isomorphic graphs.
#         list: List of unique adjacency matrices representing non-isomorphic graphs.
#     """
#     unique_graphs = []  # Store unique non-isomorphic graphs
    
#     for adj_matrix in adjacency_matrices:
#         # Convert the adjacency matrix to a bliss graph
#         n = len(adj_matrix)
#         graph = pybliss.Graph(n)
        
#         # Add edges based on the adjacency matrix
#         for i in range(n):
#             for j in range(i+1, n):
#                 if adj_matrix[i][j] == 1:
#                     graph.add_edge(i, j)
        
#         # Check if this graph is isomorphic to any existing unique graph
#         is_unique = True
#         for unique_graph in unique_graphs:
#             if are_isomorphic(graph, unique_graph):
#                 is_unique = False
#                 break
        
#         # If unique, add to the list
#         if is_unique:
#             unique_graphs.append(graph)

#     return len(unique_graphs), unique_graphs


# # Example Usage with n graphs
# adjacency_matrices = [
#     [[0, 1, 0], [1, 0, 1], [0, 1, 0]],  # Example graph 1
#     [[0, 1, 1], [1, 0, 0], [1, 0, 0]],  # Example graph 2
#     [[0, 1, 0], [1, 0, 1], [0, 1, 0]],  # Example graph 3 (isomorphic to graph 1)
#     # Add more adjacency matrices to the list for n graphs
# ]

# # Find the number of unique non-isomorphic graphs
# count, unique_graphs = find_unique_non_isomorphic_graphs(adjacency_matrices)

# print(f"Number of unique non-isomorphic graphs: {count}")












# import networkx as nx

# def are_isomorphic(graph1, graph2):
#     """
#     Check if two graphs are isomorphic using the `networkx` isomorphism function.

#     Args:
#         graph1 (nx.Graph): First graph.
#         graph2 (nx.Graph): Second graph.

#     Returns:
#         bool: True if the graphs are isomorphic, False otherwise.
#     """
#     return nx.is_isomorphic(graph1, graph2)

# def find_unique_non_isomorphic_graphs(adjacency_matrices):
#     """
#     Find unique non-isomorphic graphs from a list of adjacency matrices.

#     Args:
#         adjacency_matrices (list of lists): A list of adjacency matrices representing graphs.

#     Returns:
#         int: Number of unique non-isomorphic graphs.
#         list: List of unique adjacency matrices representing non-isomorphic graphs.
#     """
#     unique_graphs = []  # Store unique non-isomorphic graphs

#     for adj_matrix in adjacency_matrices:
#         # Convert the adjacency matrix to a networkx graph
#         n = len(adj_matrix)
#         graph = nx.Graph()
#         graph.add_nodes_from(range(n))
        
#         # Add edges based on the adjacency matrix
#         for i in range(n):
#             for j in range(i+1, n):
#                 if adj_matrix[i][j] == 1:
#                     graph.add_edge(i, j)

#         # Check if this graph is isomorphic to any existing unique graph
#         is_unique = True
#         for unique_graph in unique_graphs:
#             if are_isomorphic(graph, unique_graph):
#                 is_unique = False
#                 break

#         # If unique, add to the list
#         if is_unique:
#             unique_graphs.append(graph)

#     return len(unique_graphs), unique_graphs


# adjm_list = aj.all_adj_matrix(7) 
# #


# # Example Usage with n graphs
# adjacency_matrices = [
#     [[0, 1, 0], [1, 0, 1], [0, 1, 0]],  # Example graph 1
#     [[0, 1, 1], [1, 0, 0], [1, 0, 0]],  # Example graph 2
#     [[0, 1, 0], [1, 0, 1], [0, 1, 0]],  # Example graph 3 (isomorphic to graph 1)
#     # Add more adjacency matrices to the list for n graphs
# ]

# # Find the number of unique non-isomorphic graphs
# count, unique_graphs = find_unique_non_isomorphic_graphs(adjm_list)

# print(f"Number of unique non-isomorphic graphs: {count}")

















def are_isomorphic(graph1, graph2):
    """
    Check if two graphs are isomorphic using the `networkx` isomorphism function.

    Args:
        graph1 (nx.Graph): First graph.
        graph2 (nx.Graph): Second graph.

    Returns:
        bool: True if the graphs are isomorphic, False otherwise.
    """
    return nx.is_isomorphic(graph1, graph2)

def find_unique_non_isomorphic_graphs(adjacency_matrices):
    """
    Find unique non-isomorphic graphs from a list of adjacency matrices.

    Args:
        adjacency_matrices (list of lists): A list of adjacency matrices representing graphs.

    Returns:
        int: Number of unique non-isomorphic graphs.
        list: List of unique adjacency matrices representing non-isomorphic graphs.
    """
    unique_graphs = []  # Store unique non-isomorphic graphs

    for adj_matrix in adjacency_matrices:
        # Convert the adjacency matrix to a networkx graph
        n = len(adj_matrix)
        graph = nx.Graph()
        graph.add_nodes_from(range(n))
        
        # Add edges based on the adjacency matrix
        for i in range(n):
            for j in range(i+1, n):
                if adj_matrix[i][j] == 1:
                    graph.add_edge(i, j)

        # Check if this graph is isomorphic to any existing unique graph
        is_unique = True
        for unique_graph in unique_graphs:
            if are_isomorphic(graph, unique_graph):
                is_unique = False
                break

        # If unique, add to the list
        if is_unique:
            unique_graphs.append(graph)

    # Convert each unique graph back to an adjacency matrix (list of lists)
    unique_adj_matrices = []
    for graph in unique_graphs:
        adj_matrix_np = nx.to_numpy_array(graph)  # Convert to NumPy array
        adj_matrix_list = adj_matrix_np.astype(int).tolist()  # Convert to list of lists
        unique_adj_matrices.append(adj_matrix_list)

    return len(unique_adj_matrices), unique_adj_matrices