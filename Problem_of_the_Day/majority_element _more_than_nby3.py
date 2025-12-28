#Majority Element - More Than n/3

class Solution:
    def findMajority(self, arr):
        n = len(arr)
        if not arr:
            return []

        # Step 1: Find up to two potential majority candidates
        count1 = count2 = 0
        candidate1 = candidate2 = None

        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify if these candidates appear more than n//3 times
        result = []
        for candidate in [candidate1, candidate2]:
            if arr.count(candidate) > n // 3:
                result.append(candidate)

        return sorted(result)

#Time Complexity: O(n) where n is the length of the array.
#Space Complexity: O(1) since we are using a constant amount of space.