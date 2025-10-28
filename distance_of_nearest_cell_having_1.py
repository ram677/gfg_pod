#Distance of nearest cell having 1

from collections import deque
from typing import List

class Solution:
	def nearest(self, grid: List[List[int]]) -> List[List[int]]:
		rows, cols = len(grid), len(grid[0])
		
		# Initialize distance matrix and queue for BFS.
		distance = [[-1 for _ in range(cols)] for _ in range(rows)]
		q = deque()

		# Step 1: Find all source '1's and add them to the queue.
		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == 1:
					distance[r][c] = 0
					q.append((r, c))

		# Step 2: Perform the multi-source BFS.
		while q:
			r, c = q.popleft()
			
			# Explore 4-directional neighbors.
			for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
				nr, nc = r + dr, c + dc
				
				# Check if the neighbor is valid and unvisited.
				if 0 <= nr < rows and 0 <= nc < cols and distance[nr][nc] == -1:
					distance[nr][nc] = distance[r][c] + 1
					q.append((nr, nc))
					
		return distance
	
# Time Complexity: O(N * M) where N is the number of rows and M is the number of columns in the grid.
# Space Complexity: O(N * M) for the distance matrix and the queue in the worst case.