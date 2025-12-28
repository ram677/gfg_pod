#Minimum days to make M bouquets

class Solution:
    def minDaysBloom(self, arr, k, m):
        n = len(arr)
        # Not enough flowers at all
        if n < m * k:
            return -1

        # Function to check if we can make m bouquets by 'day'
        def canMake(day):
            bouquets = 0
            flowers = 0
            for bloom in arr:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:  # early exit
                    return True
            return bouquets >= m

        # Binary search on days
        left, right = min(arr), max(arr)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if canMake(mid):
                ans = mid
                right = mid - 1  # try smaller day
            else:
                left = mid + 1
        return ans

        
#Time Complexity: O(n⋅log(max(arr)))
#Space Complexity: O(1)
#Where n is the number of flowers and max(arr) is the maximum bloom day.