class Solution:
	def farMin(self, arr):
		n = len(arr)
		if n <= 1:
			return [-1] * n

		ans = [-1] * n

		# Step 1: Precompute an array of suffix minimums.
		# suffix_min[i] will hold the minimum value in arr[i...n-1].
		suffix_min = [0] * n
		suffix_min[n - 1] = arr[n - 1]
		for i in range(n - 2, -1, -1):
			suffix_min[i] = min(arr[i], suffix_min[i + 1])

		# Step 2: For each element arr[i], find the farthest smaller element to its right.
		for i in range(n - 1):
			target = arr[i]
			
			# Binary search on the indices to the right of i.
			low = i + 1
			high = n - 1
			farthest_idx = -1

			while low <= high:
				mid = low + (high - low) // 2
				
				# If the minimum element from mid onwards is smaller than the target,
				# a potential answer exists at or after mid. We record this and
				# search for an even farther index to the right.
				if suffix_min[mid] < target:
					farthest_idx = mid
					low = mid + 1
				else:
					# No element from mid onwards is smaller. Search left.
					high = mid - 1
		
			ans[i] = farthest_idx
			
		return ans

#Time complexity: O(n log n)
#Space complexity: O(n)
#Where n is the length of the input array.