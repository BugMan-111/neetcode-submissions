class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given an int
        # return true if there is dup
        s = set()

        # iter over the given list to find dup
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return True

        # if no dup are found return false
        return False
         