#Second Best Minimum Spanning Tree

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

class Solution:
    def secondMST(self, V, edges):
        # Sort edges by weight for Kruskal's
        edges.sort(key=lambda x: x[2])
        
        # --- Step 1: Find the Best MST ---
        dsu = DSU(V)
        mst_weight = 0
        mst_edges_indices = []
        edges_count = 0
        
        for i, (u, v, w) in enumerate(edges):
            if dsu.union(u, v):
                mst_weight += w
                mst_edges_indices.append(i)
                edges_count += 1
        
        # If the original graph isn't connected, no MST exists
        if edges_count < V - 1:
            return -1
            
        second_best_weight = float('inf')
        
        # --- Step 2: Find Second Best MST ---
        # Try removing each edge that was part of the original MST
        for excluded_index in mst_edges_indices:
            dsu_temp = DSU(V)
            current_weight = 0
            current_edges_count = 0
            
            for i, (u, v, w) in enumerate(edges):
                # Skip the edge we decided to exclude
                if i == excluded_index:
                    continue
                
                # If adding this edge creates a MST strictly larger than the original
                # that is already worse than our current second_best, we can stop early 
                # (optimization), but standard Kruskal's logic is safer.
                if dsu_temp.union(u, v):
                    current_weight += w
                    current_edges_count += 1
            
            # Check if we formed a valid spanning tree
            if current_edges_count == V - 1:
                if current_weight > mst_weight:
                    second_best_weight = min(second_best_weight, current_weight)
                    
        return second_best_weight if second_best_weight != float('inf') else -1
    
# Time Complexity: O(E log E + E * α(V)) where E is the number of edges and V is the number of vertices.
# Space Complexity: O(V) for the DSU structure.