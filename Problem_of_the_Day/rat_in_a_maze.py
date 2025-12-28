#Rat in a Maze

class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        
        # Early exit if the start or end points are blocked
        if maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []
            
        result = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        
        def findPaths(r, c, current_path):
            # Base Case: If we have reached the destination
            if r == n - 1 and c == n - 1:
                result.append(current_path)
                return

            # Mark the current cell as visited for the current path
            visited[r][c] = True

            # Explore all directions in lexicographical order: D, L, R, U
            # (dr, dc, move_char)
            moves = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]
            
            for dr, dc, move_char in moves:
                nr, nc = r + dr, c + dc
                
                # Check if the next move is valid
                if 0 <= nr < n and 0 <= nc < n and \
                   not visited[nr][nc] and maze[nr][nc] == 1:
                    findPaths(nr, nc, current_path + move_char)

            # Backtrack: Un-mark the cell so it can be used in other paths
            visited[r][c] = False

        # Start the backtracking process from the source cell (0, 0)
        findPaths(0, 0, "")
        
        return result
    
# Time Complexity: O(4^(n^2)) in the worst case, where n is the size of the maze. This is because each cell can lead to up to 4 possible directions.
# Space Complexity: O(n^2) for the visited matrix and the recursion stack in the worst case.