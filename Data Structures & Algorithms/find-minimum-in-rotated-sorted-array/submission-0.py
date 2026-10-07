class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = float('inf')
        for num in nums:
            if num < min_num:
                min_num = num
        
        return min_num
        