#Shortest Path Using Atmost One Curved Edge

import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, a: int, b: int, edges: List[List[int]]) -> int:
        # 1. Build the graph using ONLY straight edge weights (w1)
        adj = [[] for _ in range(n)]
        for u, v, w1, w2 in edges:
            adj[u].append((v, w1))
            adj[v].append((u, w1))

        # Helper function to run Dijkstra
        def get_dijkstra_dist(start_node):
            dists = [float('inf')] * n
            dists[start_node] = 0
            pq = [(0, start_node)]  # (distance, node)

            while pq:
                d, u = heapq.heappop(pq)

                # If we found a shorter path to u already, skip
                if d > dists[u]:
                    continue

                for v, weight in adj[u]:
                    if dists[u] + weight < dists[v]:
                        dists[v] = dists[u] + weight
                        heapq.heappush(pq, (dists[v], v))
            return dists

        # 2. Get shortest distances from source (a) and destination (b)
        # using only straight edges.
        dist_from_a = get_dijkstra_dist(a)
        dist_from_b = get_dijkstra_dist(b)

        # 3. Initialize answer with the path using 0 curved edges
        ans = dist_from_a[b]

        # 4. Iterate through all edges to consider using them as the ONE curved edge
        for u, v, w1, w2 in edges:
            # Consider curved edge u -> v
            if dist_from_a[u] != float('inf') and dist_from_b[v] != float('inf'):
                ans = min(ans, dist_from_a[u] + w2 + dist_from_b[v])
            
            # Consider curved edge v -> u
            if dist_from_a[v] != float('inf') and dist_from_b[u] != float('inf'):
                ans = min(ans, dist_from_a[v] + w2 + dist_from_b[u])

        # If ans is still infinity, no path exists
        if ans == float('inf'):
            return -1
            
        return ans
    
# Time Complexity: O((E + V) log V) for Dijkstra's algorithm + O(E) for checking edges, where V is number of vertices and E is number of edges.
# Space Complexity: O(V + E) for the graph representation and distance arrays.