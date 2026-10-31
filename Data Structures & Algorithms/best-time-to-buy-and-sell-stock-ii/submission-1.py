class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def recur(i, purchased_price):
            if i >= len(prices):
                return 0
            if (i, purchased_price) in cache:
                return cache[(i, purchased_price)]
            
            # decision
            # have stock
            res = 0
            if purchased_price >= 0:
                res = max(recur(i + 1, purchased_price), recur(i + 1, -1) + prices[i])
            else:
                # do not have stock
                res = max(recur(i + 1, -1), recur(i + 1, prices[i]) - prices[i])
            
            cache[(i, purchased_price)] = res
            return res

        return recur(0, -1)
            

        