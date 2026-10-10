class Solution:
    def climbStairs(self, n: int) -> int:
        # RECURSIVE - O(2^N)
        #if n == 1:
        #    return 1
        #if n == 2:
        #    return 2
        
        #return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # DP 
        memo = {}

        def dfs(i:int) -> int:
            if i == 1:
                return i
            if i == 2:
                return i
            
            if i in memo:
                return memo[i]
            
            memo[i] = dfs(i - 1) + dfs(i - 2)
            return memo[i]

        return dfs(n)
        

