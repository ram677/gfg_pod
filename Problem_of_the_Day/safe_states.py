#Safe States

from collections import deque
from typing import List

class Solution:
    def safeNodes(self, V: int, edges: List[List[int]]) -> List[int]:
        
        # 1. Build the reversed graph and count original out-degrees
        rev_adj = [[] for _ in range(V)]
        out_degree = [0] * V
        
        for u, v in edges:
            # Original edge: u -> v
            # Reversed edge: v -> u
            rev_adj[v].append(u)
            out_degree[u] += 1
            
        # 2. Initialize the queue with all terminal nodes (out-degree 0)
        q = deque()
        for i in range(V):
            if out_degree[i] == 0:
                q.append(i)
                
        safe_nodes = []
        
        # 3. Perform the topological sort
        while q:
            node = q.popleft()
            safe_nodes.append(node)
            
            # Look at all nodes that pointed to this safe node
            for neighbor in rev_adj[node]:
                # "Remove" the edge by decrementing the out-degree
                out_degree[neighbor] -= 1
                
                # If this neighbor now only points to safe nodes, it's also safe
                if out_degree[neighbor] == 0:
                    q.append(neighbor)
        
        # 4. Sort the result and return
        safe_nodes.sort()
        return safe_nodes
    
# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V + E) for the reversed graph and auxiliary data structures.