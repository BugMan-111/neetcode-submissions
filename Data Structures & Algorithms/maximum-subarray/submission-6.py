class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # reached 0 break 
        result = 0
        current = 0

        for num in nums:  
            # reached 0 abort the prev and start from the next one
            if current + num <= 0:
                current = 0
                continue
            else:
                current += num
            if current > result:
                result = current

        if result == 0:
            return max(nums)

        return result



        