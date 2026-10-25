class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # MEMOIZATION 
        # TIME - O(M X N)
        # SPACE - O(M X N)
        # memo = {}
        # def dfs(row, col):
        #     if row == m or col == n:
        #         return 0
        #     if row == m - 1 and col == n - 1:
        #         return 1
            
        #     if (row, col) in memo:
        #         return memo[(row, col)]

        #     down_paths = dfs(row + 1, col)
        #     up_paths = dfs(row, col + 1)

        #     memo[(row, col)] = down_paths + up_paths

        #     return memo[(row, col)]
        
        # return dfs(0,0)


        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
            
        return dp[m - 1][n - 1]