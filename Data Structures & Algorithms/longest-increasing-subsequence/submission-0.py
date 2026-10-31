
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[1,1]] * len(nums)
        dp[0] = [nums[0], 1]
        v = 1
        for i in range(1, len(nums)):
            # seach dp array to find the longest subseq
            result = 0
            for j in range(0, i):
                current_num, count = dp[j]
                if current_num < nums[i]:
                    result = max(result, count)
            dp[i] = [nums[i], dp[i][1] + result]
            v = max(v, dp[i][1])
            print(dp)
        return v
