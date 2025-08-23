#Smallest Positive Missing

class Solution:
    def missingNumber(self, arr: list[int]) -> int:
        n = len(arr)

        i = 0
        while i < n:
            correct_pos = arr[i] - 1
            
            if 1 <= arr[i] <= n and arr[i] != arr[correct_pos]:
                arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
            else:
                i += 1
        
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        return n + 1

#Time Complexity: O(n) where n is the length of the input array.
#Space Complexity: O(1) since we are using a constant amount of space.