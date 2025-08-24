#Mobile numeric keypad

class Solution:
    def getCount(self, n):
        if n == 1:
            return 10  # Each digit is a valid sequence

        # Movement map
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }

        # dp[i][digit] = number of sequences of length i ending at digit
        dp = [[0 for _ in range(10)] for _ in range(n + 1)]

        # Base case: length 1, 1 way to be at each digit
        for digit in range(10):
            dp[1][digit] = 1

        # Fill DP table
        for i in range(2, n + 1):
            for digit in range(10):
                for neighbor in moves[digit]:
                    dp[i][digit] += dp[i - 1][neighbor]

        # Sum all sequences of length n starting from any digit
        return sum(dp[n][digit] for digit in range(10))

#Time Complexity: O(n) where n is the length of the sequence
#Space Complexity: O(n) for the DP table