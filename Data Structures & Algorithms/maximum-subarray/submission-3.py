class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # init the max to local maximum
        result_max = max(nums)
        current = 0

        for num in nums:
            if current + num < 0:
                # break the seq
                current = 0
            else:
                current += num
            print(current)
            result_max = max(current, result_max)

        if result_max == 0:
            return max(nums)
        
        return result_max
        