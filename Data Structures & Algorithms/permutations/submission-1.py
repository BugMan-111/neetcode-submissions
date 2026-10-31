class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recur(current, prev):
            if len(prev) == len(nums):
                result.append(prev)
                return
            for i in range(0, len(nums)):
                if current == i or nums[i] in prev:
                    continue
                current_s = deepcopy(prev)
                current_s.append(nums[i])
                recur(i, current_s)
        recur(-1, [])
        return result
                
        