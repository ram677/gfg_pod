#Cutting Binary String

class Solution:
    def is_power_of_five(self, binary_str):
        if binary_str[0] == '0':
            return False
        num = int(binary_str, 2)
        while num > 1:
            if num % 5 != 0:
                return False
            num //= 5
        return num == 1

    def cuts(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # base case: empty string needs 0 cuts

        for i in range(1, n + 1):
            for j in range(i):
                substring = s[j:i]
                if self.is_power_of_five(substring):
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1

#Time Complexity: O(n^2) where n is the length of the string.
#Space Complexity: O(n) for the DP array.