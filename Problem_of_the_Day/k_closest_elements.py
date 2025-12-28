#K closest elements

class Solution:
    def printKClosest(self, arr, k, x):
        # Remove x from array if it exists
        filtered_arr = [num for num in arr if num != x]

        elements_with_distance = []
        for num in filtered_arr:
            distance = abs(num - x)
            elements_with_distance.append((num, distance))
        
        elements_with_distance.sort(key=lambda item: (item[1], -item[0]))
        
        result = []
        for i in range(k):
            result.append(elements_with_distance[i][0])
        
        return result

#Time Complexity: O(n log n) where n is the number of elements in the array
#Space Complexity: O(n) for the filtered array and distance list.