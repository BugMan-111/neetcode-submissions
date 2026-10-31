class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # have a dict that the key is the difference beteween target the current num
        # the value is just the indices of the key
        # no dup
        d = {}
        for i in range(0, len(nums)):
            d[target - nums[i]] = i


        # search the nums list to check if there are any num in nums that could match
        for i in range(0, len(nums)):
            current_num = nums[i]
            if current_num in d and i != d[current_num]:
                result = [i , d[current_num]]
                result.sort()
                return result

        return []

        
            
        