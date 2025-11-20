#Make Strings Equal

class Solution:
    def minCost(self, s, t, transform, cost):
        # There are 26 lowercase English letters
        n_chars = 26
        inf = float('inf')
        
        # Initialize distance matrix
        # dist[i][j] is the cost to transform char i to char j
        dist = [[inf] * n_chars for _ in range(n_chars)]
        
        # Distance to self is always 0
        for i in range(n_chars):
            dist[i][i] = 0
            
        # Populate initial transformation costs
        for (u_char, v_char), w in zip(transform, cost):
            u = ord(u_char) - ord('a')
            v = ord(v_char) - ord('a')
            dist[u][v] = min(dist[u][v], w)
            
        # Floyd-Warshall Algorithm to find all-pairs shortest paths
        for k in range(n_chars):
            for i in range(n_chars):
                for j in range(n_chars):
                    if dist[i][k] != inf and dist[k][j] != inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                        
        total_min_cost = 0
        
        # Iterate through both strings
        for char_s, char_t in zip(s, t):
            if char_s == char_t:
                continue
            
            u = ord(char_s) - ord('a')
            v = ord(char_t) - ord('a')
            
            # Find the best intermediate character to transform both into
            # We need to minimize: cost(s[i] -> target) + cost(t[i] -> target)
            current_pair_cost = inf
            
            for k in range(n_chars):
                if dist[u][k] != inf and dist[v][k] != inf:
                    current_pair_cost = min(current_pair_cost, dist[u][k] + dist[v][k])
            
            if current_pair_cost == inf:
                return -1
                
            total_min_cost += current_pair_cost
            
        return total_min_cost
    
# Time Complexity: O(26^3 + N) where N is the length of the strings.
# Space Complexity: O(26^2) for the distance matrix.