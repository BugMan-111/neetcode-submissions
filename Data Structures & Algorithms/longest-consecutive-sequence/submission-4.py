class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        # find the start of the sequence
        Max = 0
        for num in nums:
            # if the num is not the start of the sequence
            current_Max = 0
            if num - 1 not in s:
                while num in s:
                    num += 1
                    current_Max += 1

            Max = max(Max, current_Max)


        return Max
            
            
        
        