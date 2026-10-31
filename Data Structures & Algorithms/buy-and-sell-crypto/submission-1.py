class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        res = 0
        for p in prices:
            res = max(res, p - low)
            low = min(low, p)
        return res