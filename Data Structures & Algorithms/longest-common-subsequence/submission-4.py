class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            else: 
                skip1 = dfs(i + 1, j)
                skip2 = dfs(i, j + 1)
                memo[(i, j)] = max(skip1, skip2)

            return memo[(i,j)]
        
        return dfs(0,0)