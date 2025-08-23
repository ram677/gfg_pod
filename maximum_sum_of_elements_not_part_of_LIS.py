#Maximum sum of elements not part of LIS

class Solution:
    def nonLisMaxSum(self, arr):
        total = sum(arr)
        n = len(arr)
        if n == 0:
            return 0
        dp = [1] * n
        s = [0] * n
        for i in range(n):
            s[i] = arr[i]
            for j in range(i):
                if arr[j] < arr[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        s[i] = s[j] + arr[i]
                    elif dp[j] + 1 == dp[i]:
                        if s[j] + arr[i] < s[i]:
                            s[i] = s[j] + arr[i]
        max_len = max(dp)
        min_sum = float('inf')
        for i in range(n):
            if dp[i] == max_len:
                if s[i] < min_sum:
                    min_sum = s[i]
        return total - min_sum

#Time Complexity: O(n^2) where n is the length of the array.
#Space Complexity: O(n) for the DP arrays.