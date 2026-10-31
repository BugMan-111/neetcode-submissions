class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        s = set(nums)

        # find the start of the sequence
        Max = 0
        for num in nums:
            # if the num is not the start of the sequence
            current = num - 1
            current_Max = 0
            while current in s:
                current_Max += 1
                current -= 1
            current = num + 1
            while current in s:
                current_Max += 1
                current += 1

            Max = max(Max, current_Max)


        return Max + 1
            
            
        
        