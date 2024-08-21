#convert adjacency matrix to a dictionary with nodes as a key and the other connected nodes as a list.

def adj_mat_dict(adj_mat):
    n = len(adj_mat)
    graph = {}
    
    for i in range(n):
        node_list = []
        for j in range(n):
            if i != j and adj_mat[i][j] == 1:
                node_list.append(j)
        graph[i] = node_list
    
    return graph



# a = [[0,1,1],
#      [1,0,1],
#      [1,1,0]]

# if __name__ == "__main__":
#     b = adj_mat_dict(a)
#     print(b)