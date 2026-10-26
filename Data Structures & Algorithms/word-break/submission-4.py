class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # memo = {}
        # def dfs(i):
        #     if i == len(s):
        #         return True
        #     if i in memo:
        #         return memo[i]
        #     for word in wordDict:
        #         if s[i : i + len(word)] == word:
        #             if dfs(i + len(word)):
        #                 memo[i] = True
        #                 return True
        #     memo[i] = False
        #     return False
        
        # return dfs(0)
        
        # DP
        n = len(s)
        dp = [False] * (n + 1)

        dp[len(s)] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                
                if (i + len(word)) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                
                if dp[i]:
                    break
        
        return dp[0]
                
