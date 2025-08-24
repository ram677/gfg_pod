#Split Array Largest Sum

class Solution:
    def splitArray(self, arr, k):
        def is_possible(max_sum_allowed):
            count = 1  # at least one subarray
            curr_sum = 0
            for num in arr:
                if curr_sum + num > max_sum_allowed:
                    count += 1
                    curr_sum = num
                    if count > k:
                        return False
                else:
                    curr_sum += num
            return True

        low = max(arr)
        high = sum(arr)
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer

#Time Complexity: O(n log m) where n is the length of the array and m is the sum of the elements
#Space Complexity: O(1) for the variables used