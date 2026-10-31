class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # bounded knap
        if sum(nums) % 2 != 0:
            return False
        dp = {0 : 0}
        for num in nums:
            current_dp = deepcopy(dp)
            for sums in dp:
                current_dp[sums + num] = current_dp.get(sums + num, 0) + 1
            dp = current_dp
        target = sum(nums) // 2
        return True if target in dp and dp[target] > 1 else False

            
        