#Max DAG Edges

from typing import List

class Solution:
    def maxEdgesToAdd(self, V: int, edges: List[List[int]]) -> int:
        # 1. Get the number of existing edges.
        E = len(edges)
        
        # 2. Calculate the maximum possible edges in a DAG with V vertices.
        #    This is the same as the number of edges in a complete undirected graph, as a saturated DAG has one directed edge for every pair of vertices.
        max_possible_edges = (V * (V - 1)) // 2
        
        # 3. The number of edges we can add is the difference between the maximum possible and what we already have.
        return max_possible_edges - E
    
# Time Complexity: O(1) since the calculations are done in constant time.
# Space Complexity: O(1) as we are using a constant amount of space.
    
