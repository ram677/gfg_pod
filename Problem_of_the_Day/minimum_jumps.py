#Minimum Jumps

class Solution:
	def minJumps(self, arr):
		n = len(arr)
		# Edge case: If the array has only one element, 0 jumps are needed.
		if n <= 1:
			return 0

		# If the first element is 0, we can't move.
		if arr[0] == 0:
			return -1

		# Initialize key variables
		maxReach = arr[0]
		steps = arr[0]
		jumps = 1

		for i in range(1, n):
			# If we have reached the end, return the number of jumps
			if i == n - 1:
				return jumps

			# Update maxReach
			maxReach = max(maxReach, i + arr[i])

			# We have used a step to get to the current position
			steps -= 1

			# If we have exhausted all steps from the current jump
			if steps == 0:
				jumps += 1

				# If the current position is beyond the maximum reach, it's impossible to continue.
				if i >= maxReach:
					return -1

				# Reset steps for the new jump
				steps = maxReach - i

		return -1
	
#Time Complexity: O(n) where n is the length of the input array arr.
#Space Complexity: O(1) as we are using a constant amount of extra space.