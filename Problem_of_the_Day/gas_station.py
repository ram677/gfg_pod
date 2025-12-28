#Gas Station

class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        total_gas = 0
        current_gas = 0
        start_station = 0
        
        for i in range(n):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            
            # If current_gas becomes negative, it means we can't reach the current station
            # from our current start_station. We must try starting from the next station.
            if current_gas < 0:
                current_gas = 0
                start_station = i + 1
        
        # If total gas is negative, a solution is impossible.
        if total_gas < 0:
            return -1
        else:
            return start_station
        
#Time Complexity: O(n) where n is the number of gas stations.
#Space Complexity: O(1) as we are using a constant amount of extra space.