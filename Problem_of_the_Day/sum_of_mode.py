#Sum of Mode

from collections import defaultdict

class Solution:
    def sumOfModes(self, arr, k):
        n = len(arr)
        if k == 0: return 0
        
        freq = defaultdict(int)            # number -> count
        freq_map = defaultdict(set)        # count -> set of numbers
        max_freq = 0
        ans = 0
        
        def add(x):
            nonlocal max_freq
            old = freq[x]
            if old > 0:
                freq_map[old].discard(x)
                if not freq_map[old]:
                    del freq_map[old]
            freq[x] += 1
            new = freq[x]
            freq_map[new].add(x)
            max_freq = max(max_freq, new)
        
        def remove(x):
            nonlocal max_freq
            old = freq[x]
            freq_map[old].discard(x)
            if not freq_map[old]:
                del freq_map[old]
                if old == max_freq:
                    max_freq -= 1
            freq[x] -= 1
            if freq[x] > 0:
                freq_map[freq[x]].add(x)
        
        # Initialize first window
        for i in range(k):
            add(arr[i])
        
        # Add first mode
        ans += min(freq_map[max_freq])
        
        # Slide window
        for i in range(k, n):
            remove(arr[i-k])
            add(arr[i])
            ans += min(freq_map[max_freq])
        
        return ans

#Time complexity: O(n)
#Space complexity: O(n)
#where n is the number of elements in the input array