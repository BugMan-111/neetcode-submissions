class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        s = set()
        l = []

        def recur(nums, s, l, prev, target):
            if sum(prev) > target:
                return
            if sum(prev) == target and prev not in s:
                l.append(list(prev))
                s.add(prev)
            for i in range(0, len(nums)):
                current = deepcopy(list(prev))
                current.append(nums[i])
                current.sort()
                recur(nums, s, l, tuple(current), target)

        recur(nums, s, l, (), target)
        return l


            

        