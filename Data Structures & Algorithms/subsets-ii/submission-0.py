class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = set()
        result = []

        def recur(nums, prev, counter, s, result):
            if prev not in s:
                s.add(prev)
                result.append(list(prev))
            if counter >= len(nums):
                return 
            for i in range(counter, len(nums)):
                current = deepcopy(prev)
                current = list(current)
                current.append(nums[i])
                current.sort()
                recur(nums, tuple(current), i + 1, s, result)

        recur(nums, (), 0, s, result)

        return result


        