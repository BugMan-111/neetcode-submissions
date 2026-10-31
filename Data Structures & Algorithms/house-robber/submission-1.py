class Solution:
    def rob(self, nums: List[int]) -> int:
        d = {} 
        def recur(nums, current, d):
            if current >= len(nums):
                return 0
            if current in d:
                return d[current]
            result = 0
            for i in range(current + 2, len(nums)):
                result = max(result, recur(nums, i, d))
            if current not in d:
                d[current] = result + nums[current]
            else:
                d[current] += result + nums[current]
            return d[current] 

        return max(recur(nums, 0, d), recur(nums, 1, d))
        