#Path With Minimum Effort

import heapq

class Solution:
    def minCostPath(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        # Direction vectors for moving up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Priority Queue stores tuples: (current_max_effort, row, col)
        pq = [(0, 0, 0)]
        
        # Distance matrix to keep track of min effort to reach each cell
        # Initialize with infinity
        min_effort = [[float('inf')] * m for _ in range(n)]
        min_effort[0][0] = 0
        
        while pq:
            current_effort, r, c = heapq.heappop(pq)
            
            # If we reached the bottom-right cell, return the effort
            if r == n - 1 and c == m - 1:
                return current_effort
            
            # If we found a path to this cell with lower effort already, skip
            if current_effort > min_effort[r][c]:
                continue
            
            # Check all 4 possible directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries
                if 0 <= nr < n and 0 <= nc < m:
                    # Calculate the effort required to move to the neighbor
                    diff = abs(mat[r][c] - mat[nr][nc])
                    # The effort for the path is the max absolute difference encountered so far
                    new_effort = max(current_effort, diff)
                    
                    # If this path gives a lower effort than previously found, update and push to heap
                    if new_effort < min_effort[nr][nc]:
                        min_effort[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
                        
        return 0 # Should not be reached given constraints
    
# Time Complexity: O(N * M * log(N * M)) where N and M are the dimensions of the matrix.
# Space Complexity: O(N * M) for the min_effort matrix and priority queue.