class Solution:
    def rob(self, nums: List[int]) -> int:
        # RECURSIVE - O(2^N)
        #def dfs(i: int) -> int:
        #    if i >= len(nums):
        #        return 0
            
        #    return max(nums[i] + dfs(i + 2), dfs(i + 1))
        
        #return dfs(0)

        # DP - TOP-DOWN - O(N)
        #memo = {}

        #def dfs(i: int) -> int:
        #    if i >= len(nums):
        #        return 0
        #    if i in memo:
        #        return memo[i]

        #    memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        #    return memo[i]
        #return dfs(0)

        # DP - BOTTOM-UP - O(N)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = [0] * (n)

        dp[-1] = nums[-1]
        dp[-2] = max(nums[-1], nums[-2])

        for i in range(n - 3, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i+1])
        
        return dp[0]
        
        
