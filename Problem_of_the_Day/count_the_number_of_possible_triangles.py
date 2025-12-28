#Count the number of possible triangles

class Solution:
    def countTriangles(self, arr: list[int]) -> int:
        """
        Counts the number of possible triangles that can be formed from array elements.
        """
        n = len(arr)
        if n < 3:
            return 0

        # 1. Sort the array
        arr.sort()

        count = 0

        # 2. Fix the largest side 'c' by iterating from the end
        for i in range(n - 1, 1, -1):
            c = arr[i]
            
            # 3. Use two pointers to find the other two sides 'a' and 'b'
            left = 0
            right = i - 1

            while left < right:
                a = arr[left]
                b = arr[right]

                # Check the triangle inequality
                if a + b > c:
                    # If arr[left] + arr[right] > c, then all elements
                    # from arr[left] to arr[right-1] will also form a
                    # valid triangle with arr[right] and c.
                    # There are (right - left) such pairs.
                    count += (right - left)
                    
                    # Try a smaller second-largest side
                    right -= 1
                else:
                    # The sum a + b is too small, need a larger 'a'
                    left += 1
        
        return count

#Time Complexity: O(n^2)
#Space Complexity: O(1)
#Where n is the number of elements in the input array