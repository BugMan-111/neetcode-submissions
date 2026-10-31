class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        curr = nums[0]
        for num in nums[1:]:
            curr = curr + num if curr + num > num else num
            res = max(res, curr)
        return res


        