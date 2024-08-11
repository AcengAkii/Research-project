# making complement graphs:
    
# I want a list of rows and columns where the first column is the edge sequences and 
# the second row is the 

#pass through a single adjacency matrics
def complement_graphs(adj_mat):
    #make the ones zeros and the zeros ones
    n = len(adj_mat)
    for i in range(n):
        for j in range(n):
            adj_mat[i][j] = abs(1-adj_mat[i][j])
    return adj_mat 