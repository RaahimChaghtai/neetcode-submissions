class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Memoization
        # memo = {}
        # def dfs(remaining):
        #     if remaining == 0:
        #         return 0
        #     if remaining < 0:
        #         return float('inf')
            
        #     if remaining in memo:
        #         return memo[remaining]

        #     minCoins = float('inf')
        #     for coin in coins:
        #         result = dfs(remaining - coin)
        #         if result != float('inf'):
        #             minCoins = min(minCoins, 1+result)

        #     memo[remaining] = minCoins
        #     return memo[remaining]
        # ans = dfs(amount)
        # if ans != float('inf'):
        #     return ans
        # return -1

        # DP
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        res = dp[amount]
        if dp[amount] != float('inf'):
            return res
        return -1

