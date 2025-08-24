#Largest Divisible Subset

class Solution:
    def largestSubset(self, arr):
        if not arr:
            return []
        
        arr.sort()
        n = len(arr)

        # dp[i] = the best subset ending at arr[i]
        dp = [[num] for num in arr]

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    candidate = dp[j] + [arr[i]]
                    if len(candidate) > len(dp[i]):
                        dp[i] = candidate
                    elif len(candidate) == len(dp[i]) and candidate > dp[i]:
                        dp[i] = candidate

        # Return the lex greatest among the longest
        return max(dp, key=lambda x: (len(x), x))

#Time Complexity: O(n^2) where n is the number of elements in the array
#Space Complexity: O(n^2) for the dp array