#Get Minimum Squares

import math

class Solution:
	def minSquares(self, n: int) -> int:
		# Create a dp array, where dp[i] will store the
		# minimum number of squares that sum up to i.
		# Initialize with a large value.
		dp = [float('inf')] * (n + 1)
		
		# Base case: 0 squares are needed to sum to 0.
		dp[0] = 0
		
		# Iterate from 1 up to n
		for i in range(1, n + 1):
			# Try subtracting all possible perfect squares (j*j)
			j = 1
			while j * j <= i:
				square = j * j
				
				# We can form 'i' by taking the solution for 'i - square'
				# and adding one more square (j*j).
				dp[i] = min(dp[i], dp[i - square] + 1)
				j += 1
				
		# The final answer is the value at n
		return dp[n]
	
# Time Complexity: O(n * sqrt(n)) where n is the input number.
# Space Complexity: O(n) for the dp array.