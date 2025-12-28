#Equalize the Towers

class Solution:
    def minCost(self, heights, cost):
        n = len(heights)
        towers = sorted(zip(heights, cost))
        total_cost = sum(cost)

        cumulative_cost = 0
        for h, c in towers:
            cumulative_cost += c
            if cumulative_cost >= total_cost / 2:
                target_height = h
                break

        min_total_cost = sum(abs(h - target_height) * c for h, c in zip(heights, cost))
        return min_total_cost

#Time Complexity: O(n log n) where n is the number of towers
#Space Complexity: O(n) for the sorted list of towers