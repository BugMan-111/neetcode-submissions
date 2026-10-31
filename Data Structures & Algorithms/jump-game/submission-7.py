# every time select the one which goes further and landed on bigger index
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        counter = 0
        while True:
            # check if the current pos will not be able to jump further
            if nums[counter] == 0:
                return False
            go = nums[counter]
            # select the option from jumps
            # that has the maximum possible jump and furthest from the current index
            # and jump to zero should take less prio
            max_pos = go
            while go > 0:
                if counter + max_pos >= len(nums) - 1:
                    return True
                if nums[counter + go] + go > nums[counter + max_pos] + max_pos:
                    max_pos = go
                go -= 1
            counter = max_pos + counter

        return True
                
        