#Word Search

class Solution:
    def isWordExist(self, mat, word):
        n = len(mat)
        m = len(mat[0])
        
        def dfs(r, c, index):
            # Base Case: If we have matched all characters in the word
            if index == len(word):
                return True
            
            # Boundary checks and character match check
            if r < 0 or r >= n or c < 0 or c >= m or mat[r][c] != word[index]:
                return False
            
            # Temporarily mark the current cell as visited
            temp = mat[r][c]
            mat[r][c] = '#'
            
            # Explore all 4 possible directions: Up, Down, Left, Right
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Backtrack: Restore the original character so other paths can use it
            mat[r][c] = temp
            
            return found

        # Iterate through every cell in the grid to find the starting point
        for i in range(n):
            for j in range(m):
                # Optimization: Only start DFS if the first letter matches
                if mat[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                        
        return False
    
# Time Complexity: O(N * 3^L) where N is the number of cells in the grid and L is the length of the word.
# Space Complexity: O(L) for the recursion stack, where L is the length of the word.