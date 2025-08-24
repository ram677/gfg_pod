#Case-specific Sorting of Strings

class Solution:
    def caseSort(self, s):
        lower = sorted([ch for ch in s if ch.islower()])
        upper = sorted([ch for ch in s if ch.isupper()])

        result = []
        l_ptr, u_ptr = 0, 0

        for ch in s:
            if ch.islower():
                result.append(lower[l_ptr])
                l_ptr += 1
            else:
                result.append(upper[u_ptr])
                u_ptr += 1

        return ''.join(result)

#Time Complexity: O(n log n) where n is the length of the string
#Space Complexity: O(n) for the sorted lists