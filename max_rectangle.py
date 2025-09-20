#Max rectangle

class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        rows = len(mat)
        cols = len(mat[0])
        heights = [0] * cols
        max_area = 0

        for r in range(rows):
            # 1. Update histogram heights for the current row
            for c in range(cols):
                if mat[r][c] == 1:
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # 2. Calculate max area for the histogram represented by 'heights'
            current_area = self._largest_rectangle_in_histogram(heights)
            
            # 3. Update the overall max area
            max_area = max(max_area, current_area)
            
        return max_area

    def _largest_rectangle_in_histogram(self, heights: list[int]) -> int:
        # The stack will store indices of bars.
        stack = []
        max_area = 0
        
        # We add a virtual bar of height 0 at the end to ensure all bars
        # in the stack are processed.
        extended_heights = heights + [0]
        
        for i, h in enumerate(extended_heights):
            # While the current bar is shorter than the bar at the top of the stack,
            # we can calculate the area for the popped bar.
            while stack and extended_heights[stack[-1]] >= h:
                height = extended_heights[stack.pop()]
                
                # The width is the distance from the current bar to the one
                # that is now at the top of the stack.
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            # Push the current bar's index onto the stack.
            stack.append(i)
        
        return max_area
    
#Time Complexity: O(m * n) where m is the number of rows and n is the number of columns.
#Space Complexity: O(n) for the heights array and stack used in histogram calculation.