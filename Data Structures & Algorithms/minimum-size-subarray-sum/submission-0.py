class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        current_sum = 0
        res = len(nums) + 1
        for end, num in enumerate(nums):
            current_sum += num
            while current_sum >= target:
                res = min(res, end - start + 1)
                current_sum -= nums[start]
                start += 1
        return res if res < len(nums) + 1 else 0
            
        