class Solution:
    def climbStairs(self, n: int) -> int:
        # RECURSIVE - O(2^N)
        #if n == 1:
        #    return 1
        #if n == 2:
        #    return 2
        
        #return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # DP - O(N)
        #memo = {}

        #def dfs(i:int) -> int:
         #   if i == 1:
          #      return i
           # if i == 2:
            #    return i
            #
           # if i in memo:
            #    return memo[i]
            
           # memo[i] = dfs(i - 1) + dfs(i - 2)
           # return memo[i]

        #return dfs(n)

        # DP
        if n <= 2:
            return n
        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

