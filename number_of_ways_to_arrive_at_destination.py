#Number of Ways to Arrive at Destination

import heapq
from collections import defaultdict
import sys

class Solution:
    def countPaths(self, V, edges):
        # Create adjacency list
        adj = defaultdict(list)
        for u, v, time in edges:
            adj[u].append((v, time))
            adj[v].append((u, time))
            
        # Distance array to store shortest time to reach each node
        # Initialize with infinity
        dist = [float('inf')] * V
        dist[0] = 0
        
        # Ways array to store count of shortest paths
        # Initialize with 0, but there's 1 way to reach start node (0 cost)
        ways = [0] * V
        ways[0] = 1
        
        # Priority queue to store (current_time, node)
        # Dijkstra's algorithm processes the smallest distance first
        pq = [(0, 0)]
        
        # Modulo value usually required for large numbers, 
        # though problem statement didn't explicitly ask for modulo, 
        # it's standard for "count ways" problems.
        MOD = 10**9 + 7
        
        while pq:
            d, u = heapq.heappop(pq)
            
            # Optimization: If current d is greater than already found shortest dist, skip
            if d > dist[u]:
                continue
            
            for v, time in adj[u]:
                new_dist = d + time
                
                # Case 1: Found a strictly shorter path
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_dist, v))
                    
                # Case 2: Found another path with the same shortest duration
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
                    
        return ways[V - 1]
    
# Time Complexity: O(E log V) where E is the number of edges and V is the number of vertices.
# Space Complexity: O(V + E) for the adjacency list and O(V) for dist and ways arrays.