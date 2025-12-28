#Allocate Minimum Pages

class Solution:
    def isPossible(self, arr, k, mid):
        students = 1
        pages = 0
        for pages_in_book in arr:
            if pages + pages_in_book > mid:
                students += 1
                pages = pages_in_book
                if students > k:
                    return False
            else:
                pages += pages_in_book
        return True

    def findPages(self, arr, k):
        n = len(arr)
        if n < k:  # not enough books for students
            return -1
        
        low, high = max(arr), sum(arr)
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            if self.isPossible(arr, k, mid):
                result = mid
                high = mid - 1  # try for a smaller maximum
            else:
                low = mid + 1   # increase limit
        
        return result

#Time Complexity: O(n log m) where n is the number of books and m is the sum of all pages.
#Space Complexity: O(1) since we are using only a constant amount of space.