class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    #     memo = {}
    #     def dfs(i, prev_index):
    #         if i == len(nums):
    #             return 0

    #         if (i, prev_index) in memo:
    #             return memo[(i, prev_index)]
                
    #         exclude = dfs(i + 1, prev_index)

    #         include = 0
    #         if prev_index == -1 or nums[i] > nums[prev_index]:
    #             include = 1 + dfs(i + 1, i) 
    #         memo[(i, prev_index)] = max(include, exclude)
    #         return memo[(i, prev_index)]
        
    #     return dfs(0, -1)
    
    # DP
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
            