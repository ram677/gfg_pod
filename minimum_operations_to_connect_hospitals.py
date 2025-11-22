#Minimum Operations to Connect Hospitals

from typing import List

class Solution:
    def minConnect(self, V: int, edges: List[List[int]]) -> int:
        # Step 1: Check if we have enough edges to potentially connect the graph.
        # A graph with V vertices needs at least V-1 edges to be connected.
        if len(edges) < V - 1:
            return -1
            
        # Step 2: Build the adjacency list for the graph.
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 3: Count the number of connected components.
        visited = [False] * V
        components = 0
        
        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(V):
            if not visited[i]:
                # Found a new component
                components += 1
                # Visit all nodes in this component
                dfs(i)
                
        # Step 4: The number of operations needed is (number of components - 1).
        return components - 1
    
# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V + E) for the adjacency list and visited array.