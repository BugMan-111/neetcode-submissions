class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d = {0 : 1}
        for num in nums:
            current_d = {}
            for elements in d:
                current_d[elements + num] = current_d.get(elements + num, 0) + d.get(elements, 1) 
                current_d[elements - num] = current_d.get(elements - num, 0) + d.get(elements, 1) 
            d = current_d
        return d.get(target, 0)
            