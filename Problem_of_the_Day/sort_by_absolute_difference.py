#Sort by Absolute Difference


class Solution:
    def rearrange(self, arr, x):
        arr.sort(key=lambda num: abs(num - x))
        return arr
    
#Time complexity :  O(n log n)
#Space Complexity: O(1) 
#Whhere n is length of the array.