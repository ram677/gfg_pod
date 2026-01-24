#Josephus problem

class Solution:
    def josephus(self, n, k):
        # Initialize survivor index for n=1 (0-based index is 0)
        survivor = 0
        
        # Iteratively calculate the survivor position for circle sizes 2 to n
        for i in range(2, n + 1):
            # The formula shifts the position by k and wraps around the current circle size i
            survivor = (survivor + k) % i
            
        # Convert 0-based index to 1-based index
        return survivor + 1
    
# Time Complexity: O(n), where n is the number of people.
# Space Complexity: O(1) as we are using only a constant amount of extra space.