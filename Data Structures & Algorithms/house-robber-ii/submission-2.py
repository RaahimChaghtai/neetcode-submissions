class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def dp_answer(arr):
            if len(arr) == 1:
                return arr[0]
            dp = [0] * len(arr)

            dp[-1] = arr[-1]
            dp[-2] = max(arr[-1], arr[-2])

            for i in range(len(arr) - 3, -1, -1):
                dp[i] = max(arr[i] + dp[i + 2],dp[i + 1])
            
            return dp[0]

        return max(dp_answer(nums[:-1]), dp_answer(nums[1:])) 
        