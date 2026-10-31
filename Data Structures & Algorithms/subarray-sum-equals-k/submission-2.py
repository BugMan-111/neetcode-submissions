class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev = defaultdict(int)
        prev[0] = 1
        s, res = 0, 0
        for num in nums:
            s += num
            res += prev[s - k]
            prev[s] += 1
        return res


        