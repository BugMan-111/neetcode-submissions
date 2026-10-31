class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        ma = len(prices) * [0]
        mi = len(prices) * [0]
        ma[0] = prices[0]
        mi[0] = prices[0]
        result = max(0, ma[0] - mi[0])
        for i in range(0, len(prices) - 1):
            if prices[i + 1] < mi[i]:
                # if the new prices is lower than the recorded min
                mi[i + 1] = prices[i + 1]
                ma[i + 1] = prices[i + 1]
            else:
                # if the new prices is greater than the recorded min
                if prices[i + 1] > ma[i]:
                    # and if the new prices is also greater than the local max
                    ma[i + 1] = prices[i + 1]
                    mi[i + 1] = mi[i]
                    result = max(result, ma[i + 1] - mi[i + 1])
                else:
                    # if the new prices is between the local min and max
                    ma[i + 1] = ma[i]
                    mi[i + 1] = mi[i]
        print(mi)
        print(ma)
        return result




        