class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = {}
        def recur(i, d):
            if i >= len(cost):
                return 0
            if i in d:
                return d[i]
            
            d[i] = min(recur(i + 1, d), recur(i + 2, d)) + cost[i]
            print(d)
 
            return d[i]
        return min(recur(0, d), recur(1, d))
        