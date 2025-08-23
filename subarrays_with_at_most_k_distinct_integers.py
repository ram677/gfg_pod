#Subarrays With At Most K Distinct Integers

class Solution:
    def countAtMostK(self, arr, k):
        from collections import defaultdict

        left = 0
        count = 0
        freq = defaultdict(int)

        for right in range(len(arr)):
            if freq[arr[right]] == 0:
                k -= 1
            freq[arr[right]] += 1

            while k < 0:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    k += 1
                left += 1

            count += right - left + 1

        return count

#Time Complexity: O(n) where n is the length of the array.
#Space Complexity: O(k) for the frequency map.
#Where k is the number of distinct integers allowed in the subarrays.