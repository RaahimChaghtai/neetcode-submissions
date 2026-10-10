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

        # Create a DP array initialized with zeros
        dp = [0] * len(nums)

        # Base cases (filling from the right / end of the array)
        dp[-1] = nums[-1]  # Last house
        dp[-2] = max(nums[-1], nums[-2])  # Second to last house

        # Build the solution from right to left (n-3 down to 0)
        for i in range(len(nums) - 3, -1, -1):
            # Recurrence relation: max of (Rob current + 2 steps ahead, Skip current + 1 step ahead)
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        # The answer for the whole array starts at index 0
        dp_zero = dp[0]
        return dp_zero
        
        
