#Shortest Cycle

import collections
from typing import List

class Solution:
    def shortCycle(self, V: int, edges: List[List[int]]) -> int:
        # 1. Build the adjacency list for the graph.
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        min_cycle_len = float('inf')

        # 2. Iterate through each vertex as a potential source for a BFS.
        for i in range(V):
            # 'dist' stores shortest distance from source 'i'.
            # 'parent' tracks the BFS tree to avoid trivial back-edges.
            dist = [-1] * V
            parent = [-1] * V
            q = collections.deque()

            dist[i] = 0
            q.append(i)

            while q:
                u = q.popleft()

                for v in adj[u]:
                    if v == parent[u]:
                        # This is the edge leading back to the parent; ignore it.
                        continue
                    
                    if dist[v] == -1:
                        # If neighbor 'v' is unvisited, mark and enqueue it.
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    else:
                        # If 'v' is visited and not the parent, a cycle is found.
                        cycle_len = dist[u] + dist[v] + 1
                        min_cycle_len = min(min_cycle_len, cycle_len)

        if min_cycle_len == float('inf'):
            return -1
        else:
            return min_cycle_len

# Time Complexity: O(V * (V + E)) where V is the number of vertices and E is the number of edges.   
# Space Complexity: O(V + E) for the adjacency list and O(V) for the BFS structures.