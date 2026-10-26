class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            
            if remaining in memo:
                return memo[remaining]

            minCoins = float('inf')
            for coin in coins:
                result = dfs(remaining - coin)
                if result != float('inf'):
                    minCoins = min(minCoins, 1+result)
                    
            memo[remaining] = minCoins
            return memo[remaining]
        ans = dfs(amount)
        if ans != float('inf'):
            return ans
        return -1
