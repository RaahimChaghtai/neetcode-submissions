class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memo = {}
        # def dfs(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if text1[i] == text2[j]:
        #         memo[(i, j)] = 1 + dfs(i + 1, j + 1)
        #     else: 
        #         skip1 = dfs(i + 1, j)
        #         skip2 = dfs(i, j + 1)
        #         memo[(i, j)] = max(skip1, skip2)

        #     return memo[(i,j)]
        
        # return dfs(0,0)

        # DP
        rows = len(text1)
        cols = len(text2)
        dp = [[0] * (cols + 1) for i in range(rows + 1)]

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        return dp[0][0]