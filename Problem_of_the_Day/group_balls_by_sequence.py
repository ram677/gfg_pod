#Group Balls by Sequence

from collections import Counter

class Solution:
    def validgroup(self, arr, k):
        if len(arr) % k != 0:
            return False

        count = Counter(arr)
        unique_nums = sorted(count.keys())

        for num in unique_nums:
            freq = count[num]
            if freq > 0:
                for i in range(k):
                    if count[num + i] < freq:
                        return False
                    count[num + i] -= freq

        return True

#Time Complexity: O(n) where n is the number of elements in the array
#Space Complexity: O(n) for the frequency counter