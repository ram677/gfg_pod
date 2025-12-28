#Sort in specific order

class Solution:
    def sortIt(self, arr):
        odds = []
        evens = []
        
        # Separate odd and even numbers
        for num in arr:
            if num % 2 != 0:
                odds.append(num)
            else:
                evens.append(num)
        
        # Sort odd numbers in descending order
        odds.sort(reverse=True)
        
        # Sort even numbers in ascending order
        evens.sort()
        
        # Combine the results back into the original array
        # Modifying arr in-place as usually expected in such problems
        arr[:] = odds + evens
        return arr
    
# Time Complexity: O(n log n) due to sorting, where n is the number of elements in the array.
# Space Complexity: O(n) for storing odd and even numbers separately.