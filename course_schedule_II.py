#Course Schedule II

from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, n: int, m: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Build the graph (adjacency list) and in-degree array
        adj = defaultdict(list)
        in_degree = [0] * n
        
        for course, prereq in prerequisites:
            # Edge: prereq -> course
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # 2. Initialize the queue with nodes having 0 in-degree
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
                
        topological_order = []
        
        # 3. Process the nodes using Kahn's algorithm
        while q:
            node = q.popleft()
            topological_order.append(node)
            
            # Reduce in-degree of neighbors
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add to queue
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
                    
        # 4. Check if a valid order was found
        if len(topological_order) == n:
            return topological_order
        else:
            # A cycle was detected
            return []
        
# Time Complexity: O(n + m) where n is the number of courses and m is the number of prerequisites.   
# Space Complexity: O(n + m) for the adjacency list and in-degree array.