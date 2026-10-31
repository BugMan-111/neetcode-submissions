class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[0][:]
        for _, current_level in enumerate(triangle[1 : ]):
            new_dp = [None for _ in range(len(current_level))]
            for i in range(len(dp)):
                if new_dp[i] == None:
                    new_dp[i] = dp[i] + current_level[i]
                elif new_dp[i] != None:
                    new_dp[i] = min(new_dp[i], dp[i] + current_level[i])
                
                if new_dp[i + 1] == None:
                    new_dp[i + 1] = dp[i] + current_level[i + 1]
                elif new_dp[i + 1] != None:
                    new_dp[i + 1] = min(new_dp[i + 1], dp[i] + current_level[i + 1])
            dp = new_dp
        return min(dp)


        