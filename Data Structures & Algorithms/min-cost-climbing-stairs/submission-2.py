class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost[0], cost[1])
        dp = [1000*1000] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        result = 1000 * 1000
        for i in range(0, len(cost)):
            if i + 1 >= len(cost) or i + 2 >= len(cost):
                result = min(result, dp[i])
            else:
                # try i + 1 and i + 2
                dp[i + 1] = min(dp[i + 1], dp[i] + cost[i + 1])
                dp[i + 2] = min(dp[i + 2], dp[i] + cost[i + 2])

        return result

            
        

        