class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # 0, 1, 2, 3, amount
        dp = [10001] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        current = min(coins)
        for i in range(min(coins), amount + 1):
            # find min(coins[i]) for every amount
            for coin in coins:
                if i + coin < amount + 1 and dp[i + coin] > 1 + dp[i]:
                    dp[i+ coin] = 1 + dp[i]

        if dp[amount] == 10001:
            return -1
        return dp[amount]



        