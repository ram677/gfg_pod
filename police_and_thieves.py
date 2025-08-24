#Police and Thieves

class Solution:
    def catchThieves(self, arr, k):
        police = []
        thieves = []
        count = 0

        for i in range(len(arr)):
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thieves.append(i)

        while police and thieves:
            if abs(police[0] - thieves[0]) <= k:
                count += 1
                police.pop(0)
                thieves.pop(0)
            elif police[0] < thieves[0]:
                police.pop(0)
            else:
                thieves.pop(0)

        return count

#Time Complexity: O(n) where n is the length of the array
#Space Complexity: O(1) for the pointers