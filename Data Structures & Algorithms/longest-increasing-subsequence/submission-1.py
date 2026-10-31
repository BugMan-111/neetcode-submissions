class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i, num in enumerate(nums):
            can = 0
            for j in range(0, i):
                if num > nums[j]:
                    can = max(dp[j], can)
            dp[i] += can
        return max(dp)

        