class Solution:
    def rob(self, nums: List[int]) -> int:
        # RECURSIVE - O(2^N)
        #def dfs(i: int) -> int:
        #    if i >= len(nums):
        #        return 0
            
        #    return max(nums[i] + dfs(i + 2), dfs(i + 1))
        
        #return dfs(0)

        # DP - TOP-DOWN - O(N)
        memo = {}

        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
        return dfs(0)
