#Graph Diameter

from collections import deque
from typing import List

class Solution:
    def diameter(self, V: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list representation of the tree.
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(start_node: int):
            q = deque([(start_node, 0)])
            # A distance array can also serve as a 'visited' set.
            distances = [-1] * V
            distances[start_node] = 0
            
            farthest_node = start_node
            max_distance = 0

            while q:
                node, dist = q.popleft()

                # Update the farthest node found so far.
                if dist > max_distance:
                    max_distance = dist
                    farthest_node = node

                for neighbor in adj[node]:
                    if distances[neighbor] == -1:
                        distances[neighbor] = dist + 1
                        q.append((neighbor, dist + 1))
            
            return farthest_node, max_distance

        # Step 2: Run the first BFS from an arbitrary start (node 0).
        endpoint_A, _ = bfs(0)

        # Step 3: Run the second BFS from the endpoint found in the first run.
        # The distance found here is the diameter.
        _, tree_diameter = bfs(endpoint_A)

        return tree_diameter
    
# Time Complexity: O(V) where V is the number of vertices in the tree.
# Space Complexity: O(V) for the adjacency list and the queue in the worst case.