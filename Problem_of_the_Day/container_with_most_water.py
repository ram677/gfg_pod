#Container With Most Water

class Solution:
    def maxWater(self, arr):
        left, right = 0, len(arr) - 1
        max_area = 0
        
        while left < right:
            # Height = min of two lines
            height = min(arr[left], arr[right])
            # Width = distance between lines
            width = right - left
            # Area = height * width
            max_area = max(max_area, height * width)
            
            # Move pointer of smaller line
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

#Time Complexity: O(n)
#Space Complexity: O(1)
#Where n is the number of elements in the input array