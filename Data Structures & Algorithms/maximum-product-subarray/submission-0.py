class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]
        ma = nums[0]
        for i in range(1, len(nums)):
            current_max = max(prev_max * nums[i], prev_min * nums[i])
            current_max = max(current_max, nums[i])
            current_min = min(prev_max * nums[i], prev_min * nums[i])
            current_min = min(current_min, nums[i])
            ma = max(ma, current_max)
            prev_min = current_min
            prev_max = current_max
        return ma

        