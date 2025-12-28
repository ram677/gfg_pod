#The Knight's tour problem

class Solution:
    def knightTour(self, n: int):
        # Initialize the board with -1 to mark squares as unvisited
        board = [[-1 for _ in range(n)] for _ in range(n)]

        # Define the 8 possible L-shaped moves for a knight
        # (dr, dc) represents the change in row and column
        moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        # Place the knight at the starting position (0, 0)
        board[0][0] = 0

        # A recursive helper function to solve the tour via backtracking
        def solve(r: int, c: int, move_count: int) -> bool:
            # Base case: If all squares have been visited, the tour is complete
            if move_count == n * n:
                return True

            # Try all 8 possible moves from the current square
            for dr, dc in moves:
                nr, nc = r + dr, c + dc

                # Check if the next move is valid (within bounds and unvisited)
                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == -1:
                    # If valid, make the move
                    board[nr][nc] = move_count
                    
                    # Recurse for the next move
                    if solve(nr, nc, move_count + 1):
                        return True
                    
                    # If recursion doesn't lead to a solution, backtrack
                    board[nr][nc] = -1
            
            # If no moves from this square lead to a solution
            return False

        # Start the recursive search from (0, 0) with move count 1
        if solve(0, 0, 1):
            return board
        else:
            # If no solution is found
            return []
        
# Time Complexity: O(8^(n^2)) in the worst case, where n is the size of the board. This is because each cell can lead to up to 8 possible moves.
# Space Complexity: O(n^2) for the board and O(n^2) for the recursion stack in the worst case.