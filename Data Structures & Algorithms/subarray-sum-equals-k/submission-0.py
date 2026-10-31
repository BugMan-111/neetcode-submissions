class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev = {0:1}
        s = 0
        res = 0
        for num in nums:
            s += num
            res += prev.get(s - k, 0)
            if s in prev:
                prev[s] += 1
            else:
                prev[s] = 1
        return res


        