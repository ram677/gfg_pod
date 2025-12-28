#Top K Frequent in Array

import collections
from typing import List

class Solution:
	def topKFreq(self, arr: List[int], k: int) -> List[int]:
		"""
		Finds the top k most frequent elements in an array.
		"""
		# Step 1: Count the frequency of each number using collections.Counter.
		# For arr = [3, 1, 4, 4, 5, 2, 6, 1], this creates:
		# Counter({4: 2, 1: 2, 3: 1, 5: 1, 2: 1, 6: 1})
		counts = collections.Counter(arr)
		
		# Step 2: Sort the items based on frequency and then by value for ties.
		# We sort the (number, frequency) pairs. The lambda function creates a tuple
		# (frequency, number) as the sorting key. `reverse=True` sorts this
		# lexicographically in descending order, which perfectly matches the problem's rules.
		sorted_elements = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)
		
		# Step 3: Extract the first k numbers from the sorted list.
		result = []
		for i in range(k):
			result.append(sorted_elements[i][0])
			
		return result
	
# Time Complexity: O(N log N) due to sorting the frequency dictionary.
# Space Complexity: O(N) for storing the frequency counts.
# Where N is the number of elements in the input array.