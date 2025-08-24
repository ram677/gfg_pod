#Count the paths

class Solution:
    def countPaths(self, edges, V, src, dest):
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(10000)

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        memo = {}

        def dfs(u):
            if u == dest:
                return 1
            if u in memo:
                return memo[u]
            
            total = 0
            for v in graph[u]:
                total += dfs(v)
            memo[u] = total
            return total

        return dfs(src)

#Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
#Space Complexity: O(V) for the memoization dictionary.