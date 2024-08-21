#bron-kerbosch

#it also requires the graphs to be converted so that we have each node as a key followed by the
#defn of the other nodes its connected to.

class MaximalCliquesFinder:
    def __init__(self, graph): #initialisation, of the adj_mat as self
        self.graph = graph
        self.maximal_cliques = []

    def find_cliques(self): 
        nodes = list(self.graph.keys())
        self._extend([], nodes, []) #--compsub[], candidates, not[], this line is also how we will,
        #implement the recursion.
        # a = self.maximal_cliques
        # return a #new line to return cliques

    def _extend(self, compsub, candidates, not_set): #looping through new versions comp/cand/not
        if not candidates and not not_set: #if both 'candidate' and 'not' are empty compsub is a maximul clique
            self.maximal_cliques.append(compsub)
            
            return self.maximal_cliques.append(compsub)

        # Branch and bound: Choose a pivot
        pivot = candidates[0] if candidates else not_set[0] #1st element in candidate chosen
        #pivot = max(candidates, key=lambda node: len(self.graph[node])) #element with highest degree chosen.
        
        # Iterate through candidates not connected to the pivot
        for candidate in candidates[:]:
            if candidate in self.graph[pivot]:
                continue
            
            # New sets for recursion
            new_compsub = compsub + [candidate]
            new_candidates = [v for v in candidates if v in self.graph[candidate]]
            new_not_set = [v for v in not_set if v in self.graph[candidate]]

            # Recursive call to extend compsub
            self._extend(new_compsub, new_candidates, new_not_set)

            # Move candidate to not_set
            candidates.remove(candidate)
            not_set.append(candidate)

    def print_cliques(self):
        for clique in self.maximal_cliques: 
            print(clique)
            
    def list_of_cliques(self):
        cl = []
        for clique in self.maximal_cliques:
            cl.append(clique)
        return cl
            


# # Example usage- to only test inside this file
# if __name__ == "__main__":
#     # Define the graph as an adjacency dictionary
#     graph = {
#         0: [1, 2],
#         1: [0, 2, 3],
#         2: [0, 1, 3],
#         3: [1, 2, 4],
#         4: [3]
#     }

#     # Initialize the clique finder
#     finder = MaximalCliquesFinder(graph)
    
#     # Find and print all maximal cliques
#     finder.find_cliques()
#     finder.print_cliques()
