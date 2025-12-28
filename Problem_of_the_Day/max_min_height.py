#Max min Height

class Solution:
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        def can_achieve(min_height):
            water = [0] * (n + 1)  # difference array
            operations = 0
            curr_add = 0
            
            for i in range(n):
                curr_add += water[i]
                actual_height = arr[i] + curr_add
                
                if actual_height < min_height:
                    needed = min_height - actual_height
                    operations += needed
                    if operations > k:
                        return False
                    
                    curr_add += needed
                    if i + w < len(water):
                        water[i + w] -= needed
            
            return True
        
        low = min(arr)
        high = max(arr) + k
        answer = low
        
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return answer

#Time Complexity: O(n log m) where n is the length of the array and m is the range of heights
#Space Complexity: O(n) for the water difference array