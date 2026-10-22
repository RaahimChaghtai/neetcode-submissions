class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # RECURSIVE TOP DOWN MEMOIZATION
        # TIME - O(N^2)
        # SPACE - O(N)
        # n = len(nums)
        # memo = {n - 1: True}
        # def canReach(i):
        #     if i in memo:
        #         return memo[i]
            
        #     for jump in range(1, nums[i] + 1):
        #         if canReach(i + jump):
        #             memo[i] = True
        #             return True

        #     memo[i] = False
        #     return False
        
        # return canReach(0)

        # GREEDY
        # TIME - O(N)
        # SPACE - O(1)
        n = len(nums)
        goal = nums[n - 1]

        for i in range(n - 1, -1, -1):
            maxJump = nums[i]

            if i + maxJump >= goal:
                goal = i

        return goal == 0


        