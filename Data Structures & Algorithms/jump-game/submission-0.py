class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # RECURSIVE TOP DOWN MEMOIZATION
        # TIME - O(N^2)
        # SPACE - O(N)
        n = len(nums)
        memo = {n - 1: True}
        def canReach(i):
            if i in memo:
                return memo[i]
            
            for jump in range(1, nums[i] + 1):
                if canReach(i + jump):
                    memo[i] = True
                    return True

            memo[i] = False
            return False
        
        return canReach(0)




        