#Minimum Cost to cut a board into squares

class Solution:
    def minCost(self, n, m, x, y):
        x.sort(reverse=True)
        y.sort(reverse=True)

        horizontal_segments = 1
        vertical_segments = 1
        total_cost = 0

        i = 0  # Pointer for x (vertical cuts)
        j = 0  # Pointer for y (horizontal cuts)

        while i < len(x) and j < len(y):
            if x[i] >= y[j]:
                total_cost += x[i] * horizontal_segments
                vertical_segments += 1
                i += 1
            else:
                total_cost += y[j] * vertical_segments
                horizontal_segments += 1
                j += 1
        
        # Add remaining cuts if any
        while i < len(x):
            total_cost += x[i] * horizontal_segments
            i += 1
        
        while j < len(y):
            total_cost += y[j] * vertical_segments
            j += 1
            
        return total_cost
    
#Time Complexity: O(n log n + m log m) where n and m are the lengths of the input arrays x and y respectively, due to the sorting step.
#Space Complexity: O(1) as we are using a constant amount of extra space.