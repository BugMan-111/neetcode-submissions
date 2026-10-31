class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = [[]]

        def recur(nums, index, prev, l):
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                current = deepcopy(prev)
                current.append(nums[i])
                l.append(current)
                recur(nums, i + 1, current, l)

        recur(nums, 0, [], l)
        return l
            

        