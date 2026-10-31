# every time select the one which goes further and landed on bigger index
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(0, len(nums)):
            current_opt = nums[i]
            while current_opt > 0 and dp[i] is True:
                if i + current_opt >= len(nums) - 1:
                    return True
                dp[i + current_opt] = True
                current_opt -= 1
        return False

      
   