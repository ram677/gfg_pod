#Max Sum Increasing Subsequence

class Solution:
	def maxSumIS(self, arr):
		n = len(arr)
		
		# Initialize dp array with the original values.
		# dp[i] stores the max sum of an increasing subsequence ending at index i.
		dp = list(arr)
		
		# Compute max sum values in bottom-up manner
		for i in range(n):
			for j in range(i):
				# If arr[i] is greater than arr[j], it can extend the subsequence.
				# We check if adding arr[i] to the max sum ending at j is better 
				# than the current max sum ending at i.
				if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
					dp[i] = dp[j] + arr[i]
					
		# The result is the maximum value in the dp array
		return max(dp)
	
# Time Complexity: O(n^2) where n is the length of the input array.
# Space Complexity: O(n) for the dp array.