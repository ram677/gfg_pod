#Assign Mice Holes

class Solution:
    def assignHole(self, mices, holes):
        mices.sort()
        holes.sort()
        
        max_time = 0
        for i in range(len(mices)):
            time_taken = abs(mices[i] - holes[i])
            if time_taken > max_time:
                max_time = time_taken
                
        return max_time

#Time Complexity: O(n log n) due to sorting
#Space Complexity: O(1)
#Where n is the number of mice (or holes)