#Maximize the minimum difference between k elements

class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        
        def canPlace(mid):
            count = 1
            last = arr[0]
            for i in range(1, len(arr)):
                if arr[i] - last >= mid:
                    count += 1
                    last = arr[i]
                    if count >= k:
                        return True
            return False
        
        low, high = 0, arr[-1] - arr[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlace(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans

#Time Complexity: O(N log D), where N is the number of elements in the array and D is the range of the elements.
#Space Complexity: O(1)